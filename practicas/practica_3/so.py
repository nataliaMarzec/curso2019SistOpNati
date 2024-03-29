#!/usr/bin/env python

from hardware import *
import log


NEW = 'NEW'
RUNNING = 'RUNNING'
TERMINATE = 'TERMINATE'
WAITING = 'WAITING'
READY = 'READY'

## emulates a compiled program
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

        ## now test if last instruction is EXIT
        ## if not... add an EXIT as final instruction
        last = expanded[-1]
        if not ASM.isEXIT(last):
            expanded.append(INSTRUCTION_EXIT)

        return expanded

    def __repr__(self):
        return "Program({name}, {instructions})".format(name=self._name, instructions=self._instructions)


## emulates an Input/Output device controller (driver)
class IoDeviceController():

    def __init__(self, device):
        self._device = device
        self._waiting_queue = []
        self._currentPCB = None


    def runOperation(self, pcb, instruction):
        pair = {'pcb': pcb, 'instruction': instruction}
        pcb.state = WAITING
        if self._device.is_idle : 
            self._device.execute(instruction)
            self._currentPCB = pcb
        else:    
            self._waiting_queue.append(pair)
        

    def getFinishedPCB(self):
        finishedPCB = self._currentPCB
        self._currentPCB = None
        return finishedPCB

    #saca lo que esta en espera y lo ejecuta
    def sacarYEjecutar(self):
        if (len(self._waiting_queue) > 0) and self._device.is_idle:
            pair = self._waiting_queue.pop(0)
            #print(pair)
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
        procesoCorriendo = self._kernel._pcbTable.pcbRunnig()
        if (procesoCorriendo != None): 
            procesoCorriendo.state = TERMINATE 
            self._kernel._dispatcher.save(procesoCorriendo)
        if (len (self.kernel._readyQueue) != 0):
            siguiente_pcb = self._kernel._readyQueue.pop(0)
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
        if (len(self._kernel._readyQueue) != 0):
            pcbAEjecutar = self._kernel._readyQueue.pop(0)
            self._kernel._dispatcher.load(pcbAEjecutar) 
        
        
        log.logger.info(self.kernel.ioDeviceController)


class IoOutInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        pcb = self.kernel.ioDeviceController.getFinishedPCB() 
        if (self._kernel._pcbTable.hayPcbRunnig()):
            self._kernel._readyQueue.append(pcb)
            pcb.state = READY

        else:
            self._kernel._dispatcher.load(pcb)
        log.logger.info(self.kernel.ioDeviceController)

        self._kernel.ioDeviceController.sacarYEjecutar()

class NewInterruptionHandler(AbstractInterruptionHandler):
    def execute(self,irq):
        program = irq.parameters
        base = self.kernel._loader.load(program)
        proceso = Pcb(program,base)
        self.kernel._pcbTable.add(proceso)
        if self.kernel._pcbTable.pcbRunnig() == None:
            self.kernel._dispatcher.load(proceso)
        else:   
            self.kernel._readyQueue.append(proceso)
            proceso.state = READY
            log.logger.info("DICCIONARIO: {}--proceso: {}, base={}".format(self.kernel._pcbTable,proceso, base))
        
        log.logger.info(HARDWARE)
        
        #return tabulate(enumerate(self._cells), tablefmt='psql')
        #return "Memoria = {mem}".format(mem=self._cells)
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

# emulates the core of an Operative System
class Kernel():
    def __init__(self):

        self._loader = Loader()
        self._pcbTable = PcbTable()
        self._readyQueue = []
        self._dispatcher= Dispatcher()
        self._gantt = Gantt(self)


        ## setup interruption handlers
        killHandler = KillInterruptionHandler(self)
        HARDWARE.interruptVector.register(KILL_INTERRUPTION_TYPE, killHandler)
        ioInHandler = IoInInterruptionHandler(self)
        HARDWARE.interruptVector.register(IO_IN_INTERRUPTION_TYPE, ioInHandler)
        ioOutHandler = IoOutInterruptionHandler(self)
        HARDWARE.interruptVector.register(IO_OUT_INTERRUPTION_TYPE, ioOutHandler)

        newInterruptionHandler = NewInterruptionHandler(self)
        HARDWARE.interruptVector.register(NEW_INTERRUPTION_TYPE,newInterruptionHandler)


        HARDWARE.clock.addSubscriber(self._gantt)
        
        
        self._ioDeviceController = IoDeviceController(HARDWARE.ioDevice)



    @property
    def ioDeviceController(self):
        return self._ioDeviceController
          
    def run(self, program):
        # Kernel.run() debe hacer una interrupcion new
        newIRQ = IRQ(NEW_INTERRUPTION_TYPE, program)
        HARDWARE.interruptVector.handle(newIRQ)
        
    def run_batch(self,batch):
        for p in batch: 
            self.run(p)


    def __repr__(self):
        return "Kernel"

class Loader():
# Devuelve el base dir siguiente en donde va a comenzar el siguiente programa
    def __init__(self):
        self.next_basedir = 0
        #conoce el tamaño de cada proceso y al sumar uno pasa al otro proceso
    def load(self, program):
        progSize = len(program.instructions)
        for index in range(0, progSize):
            inst = program.instructions[index]
            HARDWARE.memory.write(index + self.next_basedir, inst)
        self.next_basedir += progSize
        return (self.next_basedir - progSize)

class Pcb ():
    def __init__(self,program,basedir):
        self._basedir = basedir
        self._program_path = program.name
        self.pid =0
        self.pc = 0
        self.state = 'NEW'
        

    #   pcb contruiye en el run del kernel y pasa a la tabla
    #   el pcb table recibe el pcb que contruye pasa por parametro el pcb
 

class PcbTable():
    def __init__(self):
        self._pid = 0 
        self.procesos = {}
        
        #3.2
      #  self.procesosCorriendo = {}
        # valor que se lo voy a pasar en el run intancia de la clase tabLa   
    #table
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
        pcb.state = 'RUNNING'  
  
    def save(self,pcb):  
        log.logger.info("SAVING:{}".format(pcb))
        pcb.pc = HARDWARE.cpu.pc
        HARDWARE.cpu.pc =-1




