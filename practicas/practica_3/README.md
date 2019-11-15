# Práctica 3
## Multiprogramación


En esta versión, la __CPU__ no accede directamente a la __Memoria__, como hace la __CPU__ para fetchear la instruccion?? Por que??

Existe un componente de hardware llamado Memory Management Unit (__MMU__) que se encarga de transformar las direcciones lógicas (relativas)  en direcciones físicas (absolutas)



## Interrupciones de I/O y Devices

En esta version del emulador agregamos los I/O Devices y el manejo de los mismos

Un I/O device es un componente de hardware (interno o externo) que realiza operaciones específicas.

Una particularidad que tienen estos dispositivos es los tiempos de ejecucion son mas extensos que los de CPU, ej: bajar un archivo de internet, imprimir un archivo, leer desde un DVD, etc.
Por otro lado, solo pueden ejecutar una operacion a la vez, con lo cual nuestro S.O. debe garantizar que no se "choquen" los pedidos de ejecucion.

Para ello implementamos un __IoDeviceController__ que es el encargado de "manejar" el device, encolando los pedidos para ir sirviendolos a medida que el dispositivo se libere.


También se incluyeron 2 interrupciones 

- __#IO_IN__
- __#IO_OUT__



## Lo que tenemos que hacer es:

- __1:__ Describir como funciona el __MMU__ y que datos necesitamos para correr un proceso

- __2:__ Implementar una version con __multiprogramación__ (donde todos los procesos se encuentran en memoria a la vez)

```python
    prg1 = Program("prg1.exe", [ASM.CPU(2)])
    prg2 = Program("prg2.exe", [ASM.CPU(4)])
    prg3 = Program("prg3.exe", [ASM.CPU(3)])

    # execute all programs
    kernel.run(prg1)
    kernel.run(prg2)
    kernel.run(prg3)
```


- __3:__ Entender las clases __IoDeviceController__, __PrinterIODevice__ y poder explicar como funcionan

- __4:__ Explicar cómo se llegan a ejecutar __IoInInterruptionHandler.execute()__ y  __IoOutInterruptionHandler.execute()__

- __5:__    Hagamos un pequeño ejercicio (sin codificarlo):

- __5.1:__ Que esta haciendo el CPU mientras se ejecuta una operación de I/O??

- __5.2:__ Si la ejecucion de una operacion de I/O (en un device) tarda 3 "ticks", cuantos ticks necesitamos para ejecuar el siguiente batch?? Cómo podemos mejorarlo??
    (tener en cuenta que en el emulador consumimos 1 tick para mandar a ejecutar la operacion a I/O)

    ```python
    prg1 = Program("prg1.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3), ASM.IO(), ASM.CPU(2)])
    prg2 = Program("prg2.exe", [ASM.CPU(4), ASM.IO(), ASM.CPU(1)])
    prg3 = Program("prg3.exe", [ASM.CPU(3)])
    ```

- __6:__ Ahora si, a programar... tenemos que "evolucionar" nuestro S.O. para que soporte __multiprogramación__  
         Cuando un proceso este en I/O, debemos cambiar el proceso corriendo por otro para optimizar el uso de __CPU__

    ```python
    # Ahora vamos a intentar ejecutar 3 programas a la vez
    ###################
    prg1 = Program("prg1.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3), ASM.IO(), ASM.CPU(2)])
    prg2 = Program("prg2.exe", [ASM.CPU(4), ASM.IO(), ASM.CPU(1)])
    prg3 = Program("prg3.exe", [ASM.CPU(3)])

    # execute all programs "concurrently"
    kernel.run(prg1)
    kernel.run(prg2)
    kernel.run(prg3)

    ## start
    HARDWARE.switchOn()

    ```



- __7:__ Implementar la interrupción #NEW
    ```python
    # Kernel.run() debe lanzar una interrupcion de #New para que se resuelva luego por el S.O. 
    ###################

    ## emulates a "system call" for programs execution
    def run(self, program):
        newIRQ = IRQ(NEW_INTERRUPTION_TYPE, program)
        self._interruptVector.handle(newIRQ)
    ```
