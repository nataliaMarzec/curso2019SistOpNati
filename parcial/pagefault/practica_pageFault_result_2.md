# Administración de Memoria: Memoria Virtual
## práctica: comparación de algoritmos de selección de víctima 

## Ejercicio 2:  

Secuencia de acceso

- 1, 4, 2, 4, 1, 3, 1  


## Solución:


### a) FIFO : 5 fallos de página


|Solicitud | 1 | 4 | 2 | 4 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 3#| 3 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 4 | 1#|
| Frame 3  |   |   | 2#| 2 | 2 | 2 | 2 | 




### b)	Optimo: 4 fallos de página



|Solicitud | 1 | 4 | 2 | 4 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 4 | 4 |
| Frame 3  |   |   | 2#| 2 | 2 | 3#| 3 | 



### c)	Least recently used (LRU): 4 fallos de página



|Solicitud | 1 | 4 | 2 | 4 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 4#| 4 | 4 | 4 | 4 | 4 |
| Frame 3  |   |   | 2#| 2 | 2 | 3#| 3 | 




#### LRU implementado con stack

|Solicitud                  | 1 | 4 | 2 | 4 | 1 | 3 | 1 |
| ------------------------- | - | - | - | - | - | - | - |  
| Más recientemente usado   | 1#| 4#| 2#| 4 | 1 | 3#| 1 | 
|                           |   | 1 | 4 | 2 | 4 | 1 | 3 | 
| menos recientemente usado |   |   | 1 | 1 | 2 | 4 | 4 |  



