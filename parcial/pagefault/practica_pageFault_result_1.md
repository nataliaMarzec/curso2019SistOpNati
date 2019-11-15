# Administración de Memoria: Memoria Virtual
## práctica: comparación de algoritmos de selección de víctima 

## Ejercicio 1:  

Secuencia de acceso

- 1, 4, 1, 5, 1, 2, 1


## Solución:


### a) FIFO : 5 fallos de página


|Solicitud | 1 | 4 | 1 | 5 | 1 | 2 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 2#| 2 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 4 | 1#|
| Frame 3  |   |   |   | 5#| 5 | 5 | 5 | 




### b)	Optimo: 4 fallos de página




|Solicitud | 1 | 4 | 1 | 5 | 1 | 2 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 2#| 2 |
| Frame 3  |   |   |   | 5#| 5 | 5 | 5 | 



### c)	Least recently used (LRU): 4 fallos de página




|Solicitud | 1 | 4 | 1 | 5 | 1 | 2 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 2#| 2 |
| Frame 3  |   |   |   | 5#| 5 | 5 | 5 | 




#### LRU implementado con stack

|Solicitud                  | 1 | 4 | 1 | 5 | 1 | 2 | 1 |
| ------------------------- | - | - | - | - | - | - | - |  
| Más recientemente usado   | 1#| 4#| 1 | 5#| 1 | 2#| 1 | 
|                           |   | 1 | 4 | 1 | 5 | 1 | 2 | 
| menos recientemente usado |   |   |   | 4 | 4 | 5 | 5 |  



