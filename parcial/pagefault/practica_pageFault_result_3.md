# Administración de Memoria: Memoria Virtual
## práctica: comparación de algoritmos de selección de víctima 

## Ejercicio 3:  

Secuencia de acceso

- 1, 2, 4, 3, 1, 2, 4


## Solución:


### a) FIFO : 7  fallos de página


|Solicitud | 1 | 2 | 4 | 3 | 1 | 2 | 4 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 3#| 3 | 3 | 4#|
| Frame 2  |   | 2#| 2 | 2 | 1#| 1 | 1 |
| Frame 3  |   |   | 4#| 4 | 4 | 2#| 2 | 




### b)	Optimo: 5 fallos de página




|Solicitud | 1 | 2 | 4 | 3 | 1 | 2 | 4 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 4#|
| Frame 2  |   | 2#| 2 | 2 | 2 | 2 | 2 |
| Frame 3  |   |   | 4#| 3#| 3 | 3 | 3 | 



### c)	Least recently used (LRU): 7 fallos de página




|Solicitud | 1 | 2 | 4 | 3 | 1 | 2 | 4 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 3#| 3 | 3 | 4#|
| Frame 2  |   | 2#| 2 | 2 | 1#| 1 | 1 |
| Frame 3  |   |   | 4#| 4 | 4 | 2#| 2 | 



#### LRU implementado con stack

|Solicitud                  | 1 | 2 | 4 | 3 | 1 | 2 | 4 |
| ------------------------- | - | - | - | - | - | - | - |  
| Más recientemente usado   | 1#| 2#| 4#| 3#| 1#| 2#| 4#| 
|                           |   | 1 | 2 | 4 | 3 | 1 | 2 | 
| menos recientemente usado |   |   | 1 | 2 | 4 | 3 | 1 |  



