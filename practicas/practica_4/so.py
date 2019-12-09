
from hardware import *
import log

NEW = 'NEW'
RUNNING = 'RUNNING'
TERMINATE = 'TERMINATE'
WAITING = 'WAITING'
READY = 'READY'

class Program():

    def __init__(self, name, instructions):
        self._name = name
        self._instructions = self.expand(instructions)

    @property
    def name(self):
        return self._name

    @property
    def instructions(self):
        return self._instructions

    def addInstr(self, instruction):
        self._instructions.append(instruction)

    def expand(self, instructions):
        expanded = []
        for i in instructions:
            if isinstance(i, list):
                expanded.extend(i)
            else:
                expanded.append(i)

        last = expanded[-1]
        if not ASM.isEXIT(last):
            expanded.append(INSTRUCTION_EXIT)

        return expanded

    def __repr__(self):
        return "Program({name}, {instructions})".format(name=self._name, instructions=self._instructions)


class IoDeviceController():

    def __init__(self, device):
        self._device = device
        self._waiting_queue = []
        self._currentPCB = None

    def runOperation(self, pcb, instruction):
        pair = {'pcb': pcb, 'instruction': instruction}
        pcb.state = WAITING
        if HARDWARE.ioDevice.is_idle : 
            self._device.execute(instruction)
            self._currentPCB = pcb
        else:    
            self._waiting_queue.append(pair)
        

    def getFinishedPCB(self):
        finishedPCB = self._currentPCB
        self._currentPCB = None
        return finishedPCB

    def sacarYEjecutar(self):
        if (len(self._waiting_queue) > 0) and self._device.is_idle:
            pair = self._waiting_queue.pop(0)
            pcb = pair['pcb']
            instruction = pair['instruction']
            self._currentPCB = pcb
            self._device.execute(instruction)


    def __repr__(self):
        return "IoDeviceController for {deviceID} running: {currentPCB} waiting: {waiting_queue}".format(deviceID=self._device.deviceId, currentPCB=self._currentPCB, waiting_queue=self._waiting_queue)

## emulates the  Interruptions Handlers
class AbstractInterruptionHandler():
    def __init__(self, kernel):
        self._kernel = kernel

    @property
    def kernel(self):
        return self._kernel

    def execute(self, irq):
        log.logger.error("-- EXECUTE MUST BE OVERRIDEN in class {classname}".format(classname=self.__class__.__name__))


class KillInterruptionHandler(AbstractInterruptionHandler):
    def execute(self, irq):
        log.logger.info("programa finalizado")
        if self._kernel._pcbTable.hayPcbRunnig():
            procesoCorriendo = self._kernel._pcbTable.pcbRunnig() 
            self._kernel._dispatcher.save(procesoCorriendo)
            procesoCorriendo.state = TERMINATE 
            
        if (len (self._kernel._scheduller._readyQueue.procesos()) >=1):
            siguiente_pcb = self._kernel._scheduller.next()
            log.logger.info("siguiente{}".format(siguiente_pcb))
            self._kernel._dispatcher.load(siguiente_pcb)        
        elif self._kernel._pcbTable.todosLosPcbsTerminaron(): 
            HARDWARE.switchOff()
            log.logger.info("GANTT: {}".format(self._kernel._gantt))
            

class IoInInterruptionHandler(AbstractInterruptionHandler):
    def execute(self, irq):
        operation = irq.parameters
        pcb = self._kernel._pcbTable.pcbRunnig()
        self._kernel._dispatcher.save(pcb)
        self.kernel.ioDeviceController.runOperation(pcb, operation)
        if (len(self._kernel._scheduller._readyQueue.pcbs) != 0):
            pcbAEjecutar = self._kernel._scheduller.next()
            self._kernel._dispatcher.load(pcbAEjecutar) 
        
        
        log.logger.info(self.kernel.ioDeviceController)


class IoOutInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        pcb = self.kernel.ioDeviceController.getFinishedPCB() 
        self._kernel._scheduller.add(pcb)
        self._kernel.ioDeviceController.sacarYEjecutar()
       
        log.logger.info(self.kernel.ioDeviceController)

class TimeHandler(AbstractInterruptionHandler):
    def execute(self, irq):
        if len (self._kernel._scheduller._readyQueue.procesos()) >= 1:
            if self._kernel._pcbTable.pcbRunnig() != None:
                log.logger.error("--pcbRunnig {}".format(self._kernel._pcbTable.pcbRunnig()))
                pcbCorriendo = self._kernel._pcbTable.pcbRunnig()
                self._kernel._scheduller.expropiar(pcbCorriendo)
        HARDWARE.timer.reset()


class NewInterruptionHandler(AbstractInterruptionHandler):
    def execute(self,irq):
        program = irq.parameters["programa"]
        priority= irq.parameters["prioridad"]
        base = self.kernel._loader.load(program)
        proceso = Pcb(program,base,priority)
        self.kernel._pcbTable.add(proceso)
     
        if self.kernel._pcbTable.pcbRunnig() == None:
            self.kernel._dispatcher.load(proceso)
        else:   
            self._kernel._scheduller.add(proceso)
            proceso.state = READY
            log.logger.info("DICCIONARIO: {}--proceso: {}, base={}".format(self.kernel._pcbTable,proceso, base))
        
        log.logger.info(HARDWARE)
        

class Gantt():
    def __init__(self,kernel):
        self._ticks = []
        self._kernel = kernel
   
    def tick (self,tickNbr):
        log.logger.info("guardando informacion de los estados de los PCBs en el tick N {}".format(tickNbr))
        pcbYEstado = dict()
        pcbTable = self._kernel._pcbTable.procesos
        for pid,pcb in pcbTable.items():
            pcbYEstado[pid] = pcb.state
        self._ticks.append(pcbYEstado)
  
    def __repr__(self):
        return tabulate(enumerate(self._ticks), tablefmt='grid')


class ReadyQueue():
    def __init__(self):
        self.pcbs = []
    def agregar (self,pcb):
        self.pcbs.append(pcb)
        pcb.state= READY
    def sacar (self):
        return self.pcbs.pop(0)
    def procesos(self):
        return self.pcbs


class Scheduller():

    def __init__(self,kernel):
        self._readyQueue = ReadyQueue()
        self._kernel=kernel
 
    def add(self, pcb):
        pass

    def next(self):
       return self._readyQueue.sacar() 

    def expropiar(self):
        pass

    def execute(self):
        log.logger.error("-- EXECUTE MUST BE OVERRIDEN in class {classname}".format(classname=self.__class__.__name__))

class RoundRobin(Scheduller):

    def add (self,pcb):
        if self._kernel._pcbTable.pcbRunnig() != None:
            self._readyQueue.agregar(pcb)
        else:
            self._kernel._dispatcher.load(pcb)
        
    def expropiar (self,pcb):
        if len(self._kernel._scheduller._readyQueue.procesos()) >= 1:
            if self._kernel._pcbTable.pcbRunnig() != None:
                corriendo= self._kernel._pcbTable.pcbRunnig()
                # log.logger.info("--pcbRunnig {}".format(corriendo)
                self._kernel._dispatcher.save(corriendo)
                self.add(corriendo)
                elSiguiente = self.next()
                self._kernel._dispatcher.load(elSiguiente)

    def _repr_(self):
        return "RoundRobin"


class PrioridadExpropiativa(Scheduller):
        def add(self,pcb):       
            if not self._kernel._pcbTable.hayPcbRunnig():   
                log.logger.error("--pcbRunnig {}".format(self._kernel._pcbTable.pcbRunnig()))
                self._kernel._dispatcher.load(pcb)
            else:
                self.expropiar(pcb)

        def ordenar(self,pcb):
            pcb.state = READY
            index = 0
            while len(self._readyQueue.pcbs) and self._readyQueue.pcbs[index].priority < pcb.priority:
                index = index + 1
            self._readyQueue.pcbs.insert(index,pcb)
    

        def expropiar(self,pcb):
            pcbCorriendo = self._kernel._pcbTable.pcbRunnig()
            
            if pcb.priority < pcbCorriendo.priority:
                self._kernel._dispatcher.save(pcbCorriendo)
                self.ordenar(pcbCorriendo)
                self._kernel._dispatcher.load(pcb)
            else:
                self.ordenar(pcb)
            
        def _repr_(self):
            return "PrioridadExpropiativa"

class PrioridadSinExpropiar(Scheduller):

    def add(self,pcb):
        if not self._kernel._pcbTable.hayPcbRunnig():
            self._kernel._dispatcher.load(pcb)
        else:
            pcb.state = READY
            index = 0
            while len(self._readyQueue.pcbs) and self._readyQueue.pcbs[index].priority < pcb.priority:
                index = index + 1
            self._readyQueue.pcbs.insert(index,pcb)

    
    def _repr_(self):
        return "PrioridadSinExpropiar"
   
class SchedullerFifo(Scheduller):

    def add(self, pcb):
        if not self._kernel._pcbTable.hayPcbRunnig():       
            self._kernel._dispatcher.load(pcb)
        else:
            self._readyQueue.agregar(pcb)

    def next(self):
       return self._readyQueue.sacar()

    def __repr__(self):
        return "FIFO"

class Kernel():
    def __init__(self):

        self._loader = Loader()
        self._pcbTable = PcbTable()
        # self._readyQueue = []
        self._dispatcher= Dispatcher()
        self._gantt = Gantt(self)
        # self._scheduller = SchedullerFifo(self)
        # self._scheduller = PrioridadSinExpropiar(self)
        # self._scheduller = PrioridadExpropiativa(self)
        self._scheduller = RoundRobin(self) 
        HARDWARE.timer.quantum=3

        killHandler = KillInterruptionHandler(self)
        HARDWARE.interruptVector.register(KILL_INTERRUPTION_TYPE, killHandler)
        ioInHandler = IoInInterruptionHandler(self)
        HARDWARE.interruptVector.register(IO_IN_INTERRUPTION_TYPE, ioInHandler)
        ioOutHandler = IoOutInterruptionHandler(self)
        HARDWARE.interruptVector.register(IO_OUT_INTERRUPTION_TYPE, ioOutHandler)
        timeHandler = TimeHandler(self)
        HARDWARE.interruptVector.register(TIMEOUT_INTERRUPTION_TYPE,timeHandler)

        newInterruptionHandler = NewInterruptionHandler(self)
        HARDWARE.interruptVector.register(NEW_INTERRUPTION_TYPE,newInterruptionHandler)

        HARDWARE.clock.addSubscriber(self._gantt)
          
        self._ioDeviceController = IoDeviceController(HARDWARE.ioDevice)


    @property
    def ioDeviceController(self):
        return self._ioDeviceController
          
    def run(self,program,priority):
        newIRQ = IRQ(NEW_INTERRUPTION_TYPE,{"programa":program,"prioridad":priority})
        HARDWARE.interruptVector.handle(newIRQ)
        #Fifo:
        # newIRQ = IRQ(NEW_INTERRUPTION_TYPE, program)      
    def run_batch(self,batch):
        for p in batch: 
            self.run(p)

    def __repr__(self):
        return "Kernel"

class Loader():

    def __init__(self):
        self.next_basedir = 0
    
    def load(self, program):
        progSize = len(program.instructions)
        for index in range(0, progSize):
            inst = program.instructions[index]
            HARDWARE.memory.write(index + self.next_basedir, inst)
        self.next_basedir += progSize
        return (self.next_basedir - progSize)

class Pcb ():
    def __init__(self,program,basedir,priority):
        self._basedir = basedir
        self._program_path = program.name
        self.pid =0
        self.pc = 0
        self.state = 'NEW'
        self.priority = priority
 
class PcbTable():
    def __init__(self):
        self._pid = 0 
        self.procesos = {}
        
    def add(self, pcb):
        _pidNuevo=self._pid
        self.procesos[_pidNuevo] = pcb
        pcb.pid = _pidNuevo
        self._pid +=1 


    def pcbRunnig(self):
        for k,v in self.procesos.items():
            if(v.state == RUNNING):
                return v
        return None

    def todosLosPcbsTerminaron(self):
        for k,v in self.procesos.items():
            if(v.state != TERMINATE):
                return False
        return True

    def hayPcbRunnig(self):
        for k,v in self.procesos.items():
            if(v.state == RUNNING):
                return True
        return False

    def pcbsReading(self):
        for k,v in self.procesos.items():
            if(v.state != READY):
                return False

        return True

    def pcbsWaiting(self):
        for k,v in self.procesos.items():
            if(v.state != WAITING):
                return False    
        return True 

class Dispatcher():   
    def load(self,pcb):
        log.logger.info("LOADING:{}".format(pcb))
        HARDWARE.cpu.pc = pcb.pc
        HARDWARE.mmu.baseDir = pcb._basedir
        pcb.state = RUNNING  
        log.logger.info(f"Proceso Corriendo: {pcb}")
        HARDWARE.timer.reset()
  
    def save(self,pcb):  
        log.logger.info("SAVING:{}".format(pcb))
        pcb.pc = HARDWARE.cpu.pc
        HARDWARE.cpu.pc =-1


















































