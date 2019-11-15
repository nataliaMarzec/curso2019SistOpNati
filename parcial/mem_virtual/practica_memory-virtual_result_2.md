# Práctica: algoritmos de selección de víctima


## Ejercicio 2

| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  110    |       350         |  0 |  1 |       | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   3    |  140    |       300         |  1 |  0 | <--   |

## Solución: 


|  Algoritmo   | Página | 
| ------------ | -----  |
| a) FIFO      |   0    | 
| b) LRU       |   3    |
| c) 2nd Chance|   0     |



### a) FIFO :  	Pág 0


| Página | **T Carga** | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|  **0** | **110** |       350         |  0 |  1 |       | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   3    |  140    |       300         |  1 |  0 | <--   |



### b)	LRU:  Pág 3


| Página | T Carga | **Última Referencia** | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  110    |       350         |  0 |  1 |       | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   **3**    |  140    |       **300**         |  1 |  0 | <--   |


### c)	Clock Second Chance:  Pág 0



| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  110    |       350         |  0 |  1 |       | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   3    |  140    |       300         |  1 |  0 | <--   |

 luego de mover la aguja y darle una segunda oportunidad a la Pág 3

| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   **0**    |  110    |       350         |  0 |  1 |  <--  | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   3    |  140    |       300         |  **0** |  0 |    |

 la "aguja" apunta a una Página con bit R = 0  (Víctima = Página 0)






