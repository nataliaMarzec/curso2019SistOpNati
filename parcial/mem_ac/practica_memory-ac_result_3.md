# Práctica: algoritmos de asignación de memoria libre

## Ejercicio 3

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
| a) 15 Kb |   B5      |   B5     |   B5      |
| b)  2 Kb |   B1      |   B3     |   B1      |
| c)  9 Kb |   B11     |   B7     |   B11     |


### Fist Fit (Primer ajuste)

a) Pedido: **15 Kb**  --> Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **2** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 38 Kb  |




b)  Pedido: **2 Kb**   -->  Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **10** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 36 Kb  |




c)  Pedido: **9 Kb**   -->    Se asigna el Bloque : **B11 (10 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11**|  **1** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 27 Kb  |






### Best Fit (Mejor ajuste)
a) Pedido: **15 Kb**  --> Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **2** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 38 Kb  |




b)  Pedido: **2 Kb**   -->  Se asigna el Bloque : **B3 (2 Kb) - tambien podria haberse usado B15 es indistinto**


Estado de la Memoria luego de asignar b)


| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 36 Kb  |




c)  Pedido: **9 Kb**   -->    Se asigna el Bloque : **B7 (10 Kb)**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| **B7** |  **1** |
| -- | --  |
| Total Libre| 27 Kb  |






### Worst Fit (Peor ajuste)

a) Pedido: **15 Kb**  --> Se asigna el Bloque : **B5 (17 Kb)**

Estado de la Memoria luego de asignar a)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| B1 |  12 |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| **B15** |  **2** |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 38 Kb  |




b)  Pedido: **2 Kb**   -->  Se asigna el Bloque : **B1 (12 Kb)**

Estado de la Memoria luego de asignar b)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B11** |  **10** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 36 Kb  |




c)  Pedido: **9 Kb**   -->    Se asigna el Bloque : **B11 (10 Kb) - tambien podria haberse usado B7 es indistinto**

Estado de la Memoria luego de asignar c)

| Bloque Libre |      Tamaño (Kb)   |
| -------------| -----------------  |
| **B111**|  **1** |
| B2 |   5 |
| B3 |   2 |
| B4 |   6 |
| B15|   2 |
| B6 |   1 |
| B7 |  10 |
| -- | --  |
| Total Libre| 27 Kb  |


