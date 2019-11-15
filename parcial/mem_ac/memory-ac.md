# Administración de Memoria: Asignación Continua
## práctica: algoritmos de asignación de memoria libre

Considerar un sistema con asignación de memoria continua en el que los huecos de memoria libre en orden son los siguientes: 10 KB, 4 KB, 20 KB, 18 KB, 7 KB. 9 KB, 12 KB, y 15 KB. Qué hueco es asignado en los siguientes pedidos de memoria?

- a) 19 Kb
- b) 13 Kb
- c) 5 Kb

Evaluar para primer ajuste, mejor ajuste y peor ajuste. 

Memoria al inicio

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B3 |  20 |
| B4 |  18 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 95 Kb  |


## Solución: 

| Pedido   | First Fit | Best Fit | Worst Fit |
| -------- | --------  | -------  | --------  |
| a) 19 Kb |   B3      |   B3     |   B3      |
| b) 13 Kb |   B4      |   B8     |   B4      |
| c)  5 Kb |   B1      |   B5     |   B8      |



### Fist Fit (Primer ajuste)

a) Pedido: **19 Kb**  --> Se asigna el Bloque : **B3 (20 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| **B13** |  **1** |
| B4 |  18 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 76 Kb  |



b)  Pedido: **13 Kb**   -->  Se asigna el Bloque : **B4 (18 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B13|   1 |
| **B14** |  **5** |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 63 Kb  |



c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B1 (10 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **5** |
| B2 |   4 |
| B13|   1 |
| B14|   5 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 58 Kb  |






### Best Fit (Mejor ajuste)

a) Pedido: **19 Kb**  --> Se asigna el Bloque : **B3 (20 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| **B13** |  **1** |
| B4 |  18 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 76 Kb  |



b)  Pedido: **13 Kb**   -->  Se asigna el Bloque : **B8 (15 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B13|   1 |
| B4 |  18 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| **B18** |  **2** |
| -- | --  |
| Total Libre| 63 Kb  |



c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B5 (7 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B13|   1 |
| B4 |  18 |
| **B15** |   **2** |
| B6 |   9 |
| B7 |  12 |
| B18|   2 |
| -- | --  |
| Total Libre| 58 Kb  |







### Worst Fit (Peor ajuste)

a) Pedido: **19 Kb**  --> Se asigna el Bloque : **B3 (20 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| **B13** |  **1** |
| B4 |  18 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 76 Kb  |



b)  Pedido: **13 Kb**   -->  Se asigna el Bloque : **B4 (18 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B13|   1 |
| **B14** |  **5** |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| B8 |  15 |
| -- | --  |
| Total Libre| 63 Kb  |



c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B8 (15 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  10 |
| B2 |   4 |
| B13|   1 |
| B14|   5 |
| B5 |   7 |
| B6 |   9 |
| B7 |  12 |
| **B18** |  **10** |
| -- | --  |
| Total Libre| 58 Kb  |





