# Práctica: algoritmos de asignación de memoria libre

## Ejercicio 2

Memoria al inicio

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 53 Kb  |


## Solución: 

| Pedido   | First Fit | Best Fit | Worst Fit |
| -------- | --------  | -------  | --------  |
| a)  5 Kb |   B1      |   B2     |   B5      |
| b) 14 Kb |   B5      |   B5     |   C1      |
| c)  3 Kb |   B11     |   B15    |   C2      |




### Fist Fit (Primer ajuste)

a) Pedido: **5 Kb**  --> Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **7** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 48 Kb  |




b)  Pedido: **14 Kb**   -->  Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B11|   7 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **3** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 34 Kb  |




c)  Pedido: **3 Kb**   -->    Se asigna el Bloque : **B11 (7 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B111**|   **4** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   3 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 31 Kb  |






### Best Fit (Mejor ajuste)
 

a) Pedido: **5 Kb**  --> Se asigna el Bloque : **B2 (5 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 48 Kb  |




b)  Pedido: **14 Kb**   -->  Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **3** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 34 Kb  |




c)  Pedido: **3 Kb**   -->    Se asigna el Bloque : **B15 (3 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B3 |   2 |
| B4 |   6 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 31 Kb  |




### Worst Fit (Peor ajuste)
 
a) Pedido: **5 Kb**  --> Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **12** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 48 Kb  |




b)  Pedido: **14 Kb**   -->  Se asigna el Bloque : **C1 (48 Kb)**

Tengo suficiente memoria libre para alocar el pedido de 14 Kb (hay 48 Kb libre)

Tengo que compactar la memoria porque no hay ningun bloque libre >= a 14 Kb


Estado de la Memoria luego de compactar 


| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| C1 |  48 |
| -- | --  |
| Total Libre| 48 Kb  |


Se asigna el pedido a  C1 generando un nuevo bloque (llamado C2)  


Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **C2** |  **34** |
| -- | --  |
| Total Libre| 34 Kb  |




c)  Pedido: **3 Kb**   -->    Se asigna el Bloque : **C2 (34 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **C3** |  **31** |
| -- | --  |
| Total Libre| 31 Kb  |

