from hardware import *
from so import *
import log


##
##  MAIN 
##
if __name__ == '__main__':
    log.setupLogger()
    log.logger.info('Starting emulator')

    ## setup our hardware and set memory size to 25 "cells"
    HARDWARE.setup(25)

    ## Switch on computer
    HARDWARE.switchOn()

    ## new create the Operative System Kernel
    # "booteamos" el sistema operativo
    kernel = Kernel()

    ##  create a program
    prg = Program("test.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3), ASM.IO(), ASM.CPU(3)]) 
    prg1 = Program("prg1.exe", [ASM.CPU(1),ASM.IO(), ASM.CPU(1)])
    prg2 = Program("prg2.exe", [ASM.CPU(2),ASM.IO(), ASM.CPU(2)])

    batch = [prg1, prg2]
    
    # execute the program
    # kernel.run(prg,2)
    # kernel.run(prg1,4)
    # kernel.run(prg2,3)
    kernel.run_batch(batch)





