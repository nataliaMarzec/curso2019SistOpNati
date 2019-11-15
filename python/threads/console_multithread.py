import threading
import time
from console import *


def start_kernel():
  #emula la ejecucion del clock del kernel
  while True:
    print("-- tick --")
    time.sleep(2)


t_kernel = threading.Thread(target=start_kernel)
t_console = threading.Thread(target=start_console)

#start threads
t_kernel.start()
t_console.start()


# join threads (syncronize ending)
t_kernel.join()
t_console.join()





######
# tengan en cuenta  que deben crear un lock a nivel de interruption manager 
# poder sincronizar los 2 threads.
#
# En el IM crear una instancia de  lock 
# todas las interrupciones deben comenzar con .acquire() y terminar con .release()
# ej:
#
# class InterruptionManager:
#
# def __init__(self):
#   self.kernelModeLock = threading.Lock()
#
# def new():
#   self.kernelModeLock.acquire()
#
#   -- Codigo del New ---
#   -- Codigo del New ---
#   -- Codigo del New ---
#
#   self.kernelModeLock.release()
#
# def kill():
#   self.kernelModeLock.acquire()
#
#   -- Codigo del Kill ---
#   -- Codigo del Kill ---
#   -- Codigo del Kill ---
#
#   self.kernelModeLock.release()
