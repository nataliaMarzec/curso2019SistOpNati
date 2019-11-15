# Práctica: algoritmos de asignación de memoria libre

## Ejercicio 1

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
| a) 10 Kb |   B1      |   B7     |   B5      |
| b)  8 Kb |   B5      |   B1     |   B1      |
| c)  5 Kb |   B2      |   B2     |   B7      |


### Fist Fit (Primer ajuste)

a) Pedido: **10 Kb**  --> Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **2** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 43 Kb  |




b)  Pedido: **8 Kb**   -->  Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B11|   2 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **9** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 35 Kb  |




c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B2 (5 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B11|   2 |
| B3 |   2 |
| B4 |   6 |
| B15|   9 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 30 Kb  |






### Best Fit (Mejor ajuste)

a) Pedido: **10 Kb**  --> Se asigna el Bloque : **B7 (10 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| -- | --  |
| Total Libre| 43 Kb  |




b)  Pedido: **8 Kb**   -->  Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **4** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| -- | --  |
| Total Libre| 35 Kb  |




c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B2 (5 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B11|   4 |
| B3 |   2 |
| B4 |   6 |
| B5 |  17 |
| B6 |   1 |
| -- | --  |
| Total Libre| 30 Kb  |







### Worst Fit (Peor ajuste)

a) Pedido: **10 Kb**  --> Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **7** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 43 Kb  |




b)  Pedido: **8 Kb**   -->  Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **4** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   7 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 35 Kb  |




c)  Pedido: **5 Kb**   -->    Se asigna el Bloque : **B7 (10 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B11|   4 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   7 |
| B6 |   1 |
| **B17** |  **5** |
| -- | --  |
| Total Libre| 30 Kb  |

