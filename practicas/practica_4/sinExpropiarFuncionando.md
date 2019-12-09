Starting emulator
 ---- SWITCH ON ---- 
---- :::: START CLOCK  ::: -----
        --------------- tick: 0 ---------------
cpu - NOOP
Handling #NEW irq with parameters = {'programa': Program(prg3.exe, ['CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'IO', 'CPU', 'CPU', 'CPU', 'EXIT']), 'prioridad': 2}
LOADING:<so.Pcb object at 0x7ffa2a062208>
Proceso Corriendo: <so.Pcb object at 0x7ffa2a062208>
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | CPU  |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | IO   |
|  9 | CPU  |
| 10 | CPU  |
| 11 | CPU  |
| 12 | EXIT |
| 13 |      |
| 14 |      |
| 15 |      |
| 16 |      |
| 17 |      |
| 18 |      |
| 19 |      |
| 20 |      |
| 21 |      |
| 22 |      |
| 23 |      |
| 24 |      |
| 25 |      |
| 26 |      |
| 27 |      |
| 28 |      |
| 29 |      |
| 30 |      |
| 31 |      |
| 32 |      |
| 33 |      |
| 34 |      |
+----+------+
Handling #NEW irq with parameters = {'programa': Program(prg1.exe, ['CPU', 'CPU', 'IO', 'CPU', 'CPU', 'CPU', 'IO', 'CPU', 'CPU', 'CPU', 'EXIT']), 'prioridad': 4}
DICCIONARIO: <so.PcbTable object at 0x7ffa2a05ae80>--proceso: <so.Pcb object at 0x7ffa2a062240>, base=13
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | CPU  |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | IO   |
|  9 | CPU  |
| 10 | CPU  |
| 11 | CPU  |
| 12 | EXIT |
| 13 | CPU  |
| 14 | CPU  |
| 15 | IO   |
| 16 | CPU  |
| 17 | CPU  |
| 18 | CPU  |
| 19 | IO   |
| 20 | CPU  |
| 21 | CPU  |
| 22 | CPU  |
| 23 | EXIT |
| 24 |      |
| 25 |      |
| 26 |      |
| 27 |      |
| 28 |      |
| 29 |      |
| 30 |      |
| 31 |      |
| 32 |      |
| 33 |      |
| 34 |      |
+----+------+
Handling #NEW irq with parameters = {'programa': Program(prg2.exe, ['CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'EXIT']), 'prioridad': 3}
DICCIONARIO: <so.PcbTable object at 0x7ffa2a05ae80>--proceso: <so.Pcb object at 0x7ffa2bec4978>, base=24
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | CPU  |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | IO   |
|  9 | CPU  |
| 10 | CPU  |
| 11 | CPU  |
| 12 | EXIT |
| 13 | CPU  |
| 14 | CPU  |
| 15 | IO   |
| 16 | CPU  |
| 17 | CPU  |
| 18 | CPU  |
| 19 | IO   |
| 20 | CPU  |
| 21 | CPU  |
| 22 | CPU  |
| 23 | EXIT |
| 24 | CPU  |
| 25 | CPU  |
| 26 | CPU  |
| 27 | CPU  |
| 28 | CPU  |
| 29 | CPU  |
| 30 | CPU  |
| 31 | EXIT |
| 32 |      |
| 33 |      |
| 34 |      |
+----+------+
        --------------- tick: 1 ---------------
cpu - Exec: CPU, PC=1
guardando informacion de los estados de los PCBs en el tick N 1
        --------------- tick: 2 ---------------
cpu - Exec: CPU, PC=2
guardando informacion de los estados de los PCBs en el tick N 2
        --------------- tick: 3 ---------------
cpu - Exec: CPU, PC=3
guardando informacion de los estados de los PCBs en el tick N 3
        --------------- tick: 4 ---------------
cpu - Exec: CPU, PC=4
guardando informacion de los estados de los PCBs en el tick N 4
        --------------- tick: 5 ---------------
cpu - Exec: CPU, PC=5
guardando informacion de los estados de los PCBs en el tick N 5
        --------------- tick: 6 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 6
        --------------- tick: 7 ---------------
cpu - Exec: CPU, PC=7
guardando informacion de los estados de los PCBs en el tick N 7
        --------------- tick: 8 ---------------
cpu - Exec: CPU, PC=8
guardando informacion de los estados de los PCBs en el tick N 8
        --------------- tick: 9 ---------------
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7ffa2a062208>
LOADING:<so.Pcb object at 0x7ffa2bec4978>
Proceso Corriendo: <so.Pcb object at 0x7ffa2bec4978>
IoDeviceController for Printer running: <so.Pcb object at 0x7ffa2a062208> waiting: []
guardando informacion de los estados de los PCBs en el tick N 9
        --------------- tick: 10 ---------------
device Printer - Busy: 1 of 3
cpu - Exec: CPU, PC=1
guardando informacion de los estados de los PCBs en el tick N 10
        --------------- tick: 11 ---------------
device Printer - Busy: 2 of 3
cpu - Exec: CPU, PC=2
guardando informacion de los estados de los PCBs en el tick N 11
        --------------- tick: 12 ---------------
device Printer - Busy: 3 of 3
cpu - Exec: CPU, PC=3
guardando informacion de los estados de los PCBs en el tick N 12
        --------------- tick: 13 ---------------
Handling #IO_OUT irq with parameters = Printer
IoDeviceController for Printer running: None waiting: []
cpu - Exec: CPU, PC=4
guardando informacion de los estados de los PCBs en el tick N 13
        --------------- tick: 14 ---------------
cpu - Exec: CPU, PC=5
guardando informacion de los estados de los PCBs en el tick N 14
        --------------- tick: 15 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 15
        --------------- tick: 16 ---------------
cpu - Exec: CPU, PC=7
guardando informacion de los estados de los PCBs en el tick N 16
        --------------- tick: 17 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7ffa2bec4978>
siguiente<so.Pcb object at 0x7ffa2a062208>
LOADING:<so.Pcb object at 0x7ffa2a062208>
Proceso Corriendo: <so.Pcb object at 0x7ffa2a062208>
guardando informacion de los estados de los PCBs en el tick N 17
        --------------- tick: 18 ---------------
cpu - Exec: CPU, PC=10
guardando informacion de los estados de los PCBs en el tick N 18
        --------------- tick: 19 ---------------
cpu - Exec: CPU, PC=11
guardando informacion de los estados de los PCBs en el tick N 19
        --------------- tick: 20 ---------------
cpu - Exec: CPU, PC=12
guardando informacion de los estados de los PCBs en el tick N 20
        --------------- tick: 21 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7ffa2a062208>
siguiente<so.Pcb object at 0x7ffa2a062240>
LOADING:<so.Pcb object at 0x7ffa2a062240>
Proceso Corriendo: <so.Pcb object at 0x7ffa2a062240>
guardando informacion de los estados de los PCBs en el tick N 21
        --------------- tick: 22 ---------------
cpu - Exec: CPU, PC=1
guardando informacion de los estados de los PCBs en el tick N 22
        --------------- tick: 23 ---------------
cpu - Exec: CPU, PC=2
guardando informacion de los estados de los PCBs en el tick N 23
        --------------- tick: 24 ---------------
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7ffa2a062240>
IoDeviceController for Printer running: <so.Pcb object at 0x7ffa2a062240> waiting: []
guardando informacion de los estados de los PCBs en el tick N 24
        --------------- tick: 25 ---------------
device Printer - Busy: 1 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 25
        --------------- tick: 26 ---------------
device Printer - Busy: 2 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 26
        --------------- tick: 27 ---------------
device Printer - Busy: 3 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 27
        --------------- tick: 28 ---------------
Handling #IO_OUT irq with parameters = Printer
LOADING:<so.Pcb object at 0x7ffa2a062240>
Proceso Corriendo: <so.Pcb object at 0x7ffa2a062240>
IoDeviceController for Printer running: None waiting: []
cpu - Exec: CPU, PC=4
guardando informacion de los estados de los PCBs en el tick N 28
        --------------- tick: 29 ---------------
cpu - Exec: CPU, PC=5
guardando informacion de los estados de los PCBs en el tick N 29
        --------------- tick: 30 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 30
        --------------- tick: 31 ---------------
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7ffa2a062240>
IoDeviceController for Printer running: <so.Pcb object at 0x7ffa2a062240> waiting: []
guardando informacion de los estados de los PCBs en el tick N 31
        --------------- tick: 32 ---------------
device Printer - Busy: 1 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 32
        --------------- tick: 33 ---------------
device Printer - Busy: 2 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 33
        --------------- tick: 34 ---------------
device Printer - Busy: 3 of 3
cpu - NOOP
guardando informacion de los estados de los PCBs en el tick N 34
        --------------- tick: 35 ---------------
Handling #IO_OUT irq with parameters = Printer
LOADING:<so.Pcb object at 0x7ffa2a062240>
Proceso Corriendo: <so.Pcb object at 0x7ffa2a062240>
IoDeviceController for Printer running: None waiting: []
cpu - Exec: CPU, PC=8
guardando informacion de los estados de los PCBs en el tick N 35
        --------------- tick: 36 ---------------
cpu - Exec: CPU, PC=9
guardando informacion de los estados de los PCBs en el tick N 36
        --------------- tick: 37 ---------------
cpu - Exec: CPU, PC=10
guardando informacion de los estados de los PCBs en el tick N 37
        --------------- tick: 38 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7ffa2a062240>
 ---- SWITCH OFF ---- 
GANTT: +----+------------------------------------------------+
|  0 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  1 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  2 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  3 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  4 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  5 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  6 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  7 | {0: 'RUNNING', 1: 'READY', 2: 'READY'}         |
+----+------------------------------------------------+
|  8 | {0: 'WAITING', 1: 'READY', 2: 'RUNNING'}       |
+----+------------------------------------------------+
|  9 | {0: 'WAITING', 1: 'READY', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 10 | {0: 'WAITING', 1: 'READY', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 11 | {0: 'WAITING', 1: 'READY', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 12 | {0: 'READY', 1: 'READY', 2: 'RUNNING'}         |
+----+------------------------------------------------+
| 13 | {0: 'READY', 1: 'READY', 2: 'RUNNING'}         |
+----+------------------------------------------------+
| 14 | {0: 'READY', 1: 'READY', 2: 'RUNNING'}         |
+----+------------------------------------------------+
| 15 | {0: 'READY', 1: 'READY', 2: 'RUNNING'}         |
+----+------------------------------------------------+
| 16 | {0: 'RUNNING', 1: 'READY', 2: 'TERMINATE'}     |
+----+------------------------------------------------+
| 17 | {0: 'RUNNING', 1: 'READY', 2: 'TERMINATE'}     |
+----+------------------------------------------------+
| 18 | {0: 'RUNNING', 1: 'READY', 2: 'TERMINATE'}     |
+----+------------------------------------------------+
| 19 | {0: 'RUNNING', 1: 'READY', 2: 'TERMINATE'}     |
+----+------------------------------------------------+
| 20 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 21 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 22 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 23 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 24 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 25 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 26 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 27 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 28 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 29 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 30 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 31 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 32 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 33 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 34 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 35 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 36 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
guardando informacion de los estados de los PCBs en el tick N 38