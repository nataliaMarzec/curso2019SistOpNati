#!/usr/bin/python3
import _thread
import time


# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: #%s - %s" % ( threadName, count, time.ctime(time.time()) ))

def main():
  # Create two threads as follows
  try:
     _thread.start_new_thread( print_time, ("Thread-1", 3, ) )
     _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
  except:
     print ("Error: unable to start thread")

  while 1:
     pass


# Código estándar para llamar main() cuando arranxca en programa.
if __name__ == '__main__':
    main()   