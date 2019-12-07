--- :::: START CLOCK  ::: -----
        --------------- tick: 0 ---------------
Handling #NEW irq with parameters = {'programa': Program(prg3.exe, ['CPU', 'CPU', 'CPU', 'CPU', 'IO', 'CPU', 'CPU', 'CPU', 'EXIT']), 'prioridad': 2}
LOADING:<so.Pcb object at 0x7f2e9f5e6240>
Proceso Corriendo: <so.Pcb object at 0x7f2e9f5e6240>
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | IO   |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | EXIT |
|  9 |      |
| 10 |      |
| 11 |      |
| 12 |      |
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
DICCIONARIO: <so.PcbTable object at 0x7f2e9f5e0eb8>--proceso: <so.Pcb object at 0x7f2e9f5e6278>, base=9
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | IO   |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | EXIT |
|  9 | CPU  |
| 10 | CPU  |
| 11 | IO   |
| 12 | CPU  |
| 13 | CPU  |
| 14 | CPU  |
| 15 | IO   |
| 16 | CPU  |
| 17 | CPU  |
| 18 | CPU  |
| 19 | EXIT |
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
cpu - NOOP
Handling #NEW irq with parameters = {'programa': Program(prg2.exe, ['CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'CPU', 'EXIT']), 'prioridad': 3}
guardando informacion de los estados de los PCBs en el tick N 0
DICCIONARIO: <so.PcbTable object at 0x7f2e9f5e0eb8>--proceso: <so.Pcb object at 0x7f2ea144a978>, base=20
HARDWARE state CPU(PC=0)
+----+------+
|  0 | CPU  |
|  1 | CPU  |
|  2 | CPU  |
|  3 | CPU  |
|  4 | IO   |
|  5 | CPU  |
|  6 | CPU  |
|  7 | CPU  |
|  8 | EXIT |
|  9 | CPU  |
| 10 | CPU  |
| 11 | IO   |
| 12 | CPU  |
| 13 | CPU  |
| 14 | CPU  |
| 15 | IO   |
| 16 | CPU  |
| 17 | CPU  |
| 18 | CPU  |
| 19 | EXIT |
| 20 | CPU  |
| 21 | CPU  |
| 22 | CPU  |
| 23 | CPU  |
| 24 | CPU  |
| 25 | CPU  |
| 26 | CPU  |
| 27 | EXIT |
| 28 |      |
| 29 |      |
| 30 |      |
| 31 |      |
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
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7f2e9f5e6240>
LOADING:<so.Pcb object at 0x7f2e9f5e6278>
Proceso Corriendo: <so.Pcb object at 0x7f2e9f5e6278>
IoDeviceController for Printer running: <so.Pcb object at 0x7f2e9f5e6240> waiting: []
guardando informacion de los estados de los PCBs en el tick N 5
        --------------- tick: 6 ---------------
device Printer - Busy: 1 of 3
cpu - Exec: CPU, PC=1
guardando informacion de los estados de los PCBs en el tick N 6
        --------------- tick: 7 ---------------
device Printer - Busy: 2 of 3
cpu - Exec: CPU, PC=2
guardando informacion de los estados de los PCBs en el tick N 7
        --------------- tick: 8 ---------------
device Printer - Busy: 3 of 3
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7f2e9f5e6278>
LOADING:<so.Pcb object at 0x7f2ea144a978>
Proceso Corriendo: <so.Pcb object at 0x7f2ea144a978>
IoDeviceController for Printer running: <so.Pcb object at 0x7f2e9f5e6240> waiting: [{'pcb': <so.Pcb object at 0x7f2e9f5e6278>, 'instruction': 'IO'}]
guardando informacion de los estados de los PCBs en el tick N 8
        --------------- tick: 9 ---------------
Handling #IO_OUT irq with parameters = Printer
IoDeviceController for Printer running: <so.Pcb object at 0x7f2e9f5e6278> waiting: []
cpu - Exec: CPU, PC=1
guardando informacion de los estados de los PCBs en el tick N 9
        --------------- tick: 10 ---------------
device Printer - Busy: 1 of 3
cpu - Exec: CPU, PC=2
guardando informacion de los estados de los PCBs en el tick N 10
        --------------- tick: 11 ---------------
device Printer - Busy: 2 of 3
cpu - Exec: CPU, PC=3
guardando informacion de los estados de los PCBs en el tick N 11
        --------------- tick: 12 ---------------
device Printer - Busy: 3 of 3
cpu - Exec: CPU, PC=4
guardando informacion de los estados de los PCBs en el tick N 12
        --------------- tick: 13 ---------------
Handling #IO_OUT irq with parameters = Printer
IoDeviceController for Printer running: None waiting: []
cpu - Exec: CPU, PC=5
guardando informacion de los estados de los PCBs en el tick N 13
        --------------- tick: 14 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 14
        --------------- tick: 15 ---------------
cpu - Exec: CPU, PC=7
guardando informacion de los estados de los PCBs en el tick N 15
        --------------- tick: 16 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7f2ea144a978>
LOADING:<so.Pcb object at 0x7f2e9f5e6240>
Proceso Corriendo: <so.Pcb object at 0x7f2e9f5e6240>
guardando informacion de los estados de los PCBs en el tick N 16
        --------------- tick: 17 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 17
        --------------- tick: 18 ---------------
cpu - Exec: CPU, PC=7
guardando informacion de los estados de los PCBs en el tick N 18
        --------------- tick: 19 ---------------
cpu - Exec: CPU, PC=8
guardando informacion de los estados de los PCBs en el tick N 19
        --------------- tick: 20 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7f2e9f5e6240>
LOADING:<so.Pcb object at 0x7f2e9f5e6278>
Proceso Corriendo: <so.Pcb object at 0x7f2e9f5e6278>
guardando informacion de los estados de los PCBs en el tick N 20
        --------------- tick: 21 ---------------
cpu - Exec: CPU, PC=4
guardando informacion de los estados de los PCBs en el tick N 21
        --------------- tick: 22 ---------------
cpu - Exec: CPU, PC=5
guardando informacion de los estados de los PCBs en el tick N 22
        --------------- tick: 23 ---------------
cpu - Exec: CPU, PC=6
guardando informacion de los estados de los PCBs en el tick N 23
        --------------- tick: 24 ---------------
Handling #IO_IN irq with parameters = IO
SAVING:<so.Pcb object at 0x7f2e9f5e6278>
IoDeviceController for Printer running: <so.Pcb object at 0x7f2e9f5e6278> waiting: []
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
LOADING:<so.Pcb object at 0x7f2e9f5e6278>
Proceso Corriendo: <so.Pcb object at 0x7f2e9f5e6278>
IoDeviceController for Printer running: None waiting: []
cpu - Exec: CPU, PC=8
guardando informacion de los estados de los PCBs en el tick N 28
        --------------- tick: 29 ---------------
cpu - Exec: CPU, PC=9
guardando informacion de los estados de los PCBs en el tick N 29
        --------------- tick: 30 ---------------
cpu - Exec: CPU, PC=10
guardando informacion de los estados de los PCBs en el tick N 30
        --------------- tick: 31 ---------------
Handling #KILL irq with parameters = None
programa finalizado
SAVING:<so.Pcb object at 0x7f2e9f5e6278>
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
|  5 | {0: 'WAITING', 1: 'RUNNING', 2: 'READY'}       |
+----+------------------------------------------------+
|  6 | {0: 'WAITING', 1: 'RUNNING', 2: 'READY'}       |
+----+------------------------------------------------+
|  7 | {0: 'WAITING', 1: 'RUNNING', 2: 'READY'}       |
+----+------------------------------------------------+
|  8 | {0: 'WAITING', 1: 'WAITING', 2: 'RUNNING'}     |
+----+------------------------------------------------+
|  9 | {0: 'READY', 1: 'WAITING', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 10 | {0: 'READY', 1: 'WAITING', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 11 | {0: 'READY', 1: 'WAITING', 2: 'RUNNING'}       |
+----+------------------------------------------------+
| 12 | {0: 'READY', 1: 'WAITING', 2: 'RUNNING'}       |
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
| 23 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 24 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 25 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 26 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 27 | {0: 'TERMINATE', 1: 'WAITING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 28 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 29 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
| 30 | {0: 'TERMINATE', 1: 'RUNNING', 2: 'TERMINATE'} |
+----+------------------------------------------------+
guardando informacion de los estados de los PCBs en el tick N 31