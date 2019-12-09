from hardware import *
from so import *
import log


if __name__ == '__main__':
    log.setupLogger()
    log.logger.info('Starting emulator')

    HARDWARE.setup(35)
    HARDWARE.switchOn()

    kernel = Kernel()
    
    prg3 = Program("prg3.exe", [ASM.CPU(8), ASM.IO(), ASM.CPU(3)])
    prg1 = Program("prg1.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3), ASM.IO(), ASM.CPU(3)])
    prg2 = Program("prg2.exe", [ASM.CPU(7)])

    kernel.run(prg3,2)
    kernel.run(prg1,4)
    kernel.run(prg2,3)


