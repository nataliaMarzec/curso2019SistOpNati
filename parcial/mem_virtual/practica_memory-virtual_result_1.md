# Práctica: algoritmos de selección de víctima


## Ejercicio 1

| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  150    |       325         |  1 |  1 |       | 
|   1    |  245    |       245         |  0 |  1 | <--   |
|   2    |  220    |       220         |  1 |  0 |       |
|   3    |  100    |       350         |  0 |  0 |       |


## Solución: 


|  Algoritmo   | Página | 
| ------------ | -----  |
| a) FIFO      |   3    | 
| b) LRU       |   2    |
| c) 2nd Chance|   1    |



### a) FIFO :  	Pág 3


| Página | **T Carga** | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  150    |       325         |  1 |  1 |       | 
|   1    |  245    |       245         |  0 |  1 | <--   |
|   2    |  220    |       220         |  1 |  0 |       |
| **3**  |  **100**|       350         |  0 |  0 |       |



### b)	LRU:  Pág 2


| Página | T Carga | **Última Referencia** | R  |  M | Aguja | 
| -------| ------- | --------------------- | -- | -- | ----- |
|   0    |  150    |       325         |  1 |  1 |       | 
|   1    |  245    |       245         |  0 |  1 | <--   |
| **2**  |  220    |    **220**        |  1 |  0 |       |
|   3    |  100    |       350         |  0 |  0 |       |



### c)	Clock Second Chance:  Pág 1


| Página | T Carga | Última Referencia | **R**  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  150    |       325         |  1 |  1 |       | 
| **1**  |  245    |       245         |**0**|  1 | <--   |
|   2    |  220    |       220         |  1 |  0 |       |
|   3    |  100    |       350         |  0 |  0 |       |




 la "aguja" apunta a una Página con bit R = 0  (Víctima = Página 3)






