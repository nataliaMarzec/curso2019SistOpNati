# Práctica: algoritmos de selección de víctima


## Ejercicio 3



| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  200    |       245         |  1 |  0 |       | 
|   1    |  201    |       210         |  1 |  1 |       |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  1 |  1 | <--   |


## Solución: 


|  Algoritmo   | Página | 
| ------------ | -----  |
| a) FIFO      |   2    | 
| b) LRU       |   1    |
| c) 2nd Chance|   3    |



### a) FIFO :  	Pág 2


| Página | **T Carga** | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  200    |       245         |  1 |  0 |       | 
|   1    |  201    |       210         |  1 |  1 |       |
| **2**  | **185** |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  1 |  1 | <--   |



### b)	LRU:  Pág 1


| Página | T Carga | **Última Referencia** | R  |  M | Aguja | 
| -------| ------- | --------------------- | -- | -- | ----- | 
|   0    |  200    |       245         |  1 |  0 |       | 
| **1**  |  201    |     **210**       |  1 |  1 |       |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  1 |  1 | <--   |


### c)	Clock Second Chance:  Pág 3


| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- | 
|   0    |  200    |       245         |  1 |  0 |       | 
|   1    |  201    |       210         |  1 |  1 |       |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  1 |  1 | <--   |


 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 3)


| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- | 
|   0    |  200    |       245         |  1 |  0 |  <--  | 
|   1    |  201    |       210         |  1 |  1 |       |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |**0**| 1 |       |


 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 0)

| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- | 
|   0    |  200    |       245         |**0**| 0 |       | 
|   1    |  201    |       210         |  1 |  1 |   <-- |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  0 |  1 |       |


 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 1)

| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- | 
|   0    |  200    |       245         |  0 | 0  |       | 
|   1    |  201    |       210         |**0**| 1 |       |
|   2    |  185    |       233         |  1 |  0 |   <-- |
|   3    |  220    |       230         |  0 |  1 |       |

 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 2)

| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- | 
|   0    |  200    |       245         |  0 | 0  |       | 
|   1    |  201    |       210         |  0 | 1  |       |
|   2    |  185    |       233         |**0**| 0 |       |
|   **3**    |  220    |       230         |  0 |  1 |   <-- |

 la "aguja" apunta a una Página con bit R = 0  (Víctima = Página 3)