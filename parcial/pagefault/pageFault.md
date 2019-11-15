# Administración de Memoria: Memoria Virtual
## práctica: comparación de algoritmos de selección de víctima 


Dada una memoria con 3 marcos disponibles y la siguiente secuencia de acceso a páginas:

- 1, 2, 3, 1, 4, 1, 5, 1, 2, 1, 3, 1


Calcular cuantos fallos de página (#PageFault) se producen con cada algoritmo de selección de victima:

- a) First In Fist Out (FIFO)
- b) Optimo
- c) Least Recently Used (LRU)




## Solución: 


### a) FIFO : 9 fallos de página


|Solicitud | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | 2 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 4#| 4 | 4 | 4 | 2#| 2 | 2 | 2 |
| Frame 2  |   | 2#| 2 | 2 | 2 | 1#| 1 | 1 | 1 | 1 | 3#| 3 |
| Frame 3  |   |   | 3#| 3 | 3 | 3 | 5#| 5 | 5 | 5 | 5 | 1#| 




### b)	Optimo: 6 fallos de página




|Solicitud | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | 2 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 2#| 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Frame 3  |   |   | 3#| 3 | 4#| 4 | 5#| 5 | 5 | 5 | 3#| 3 | 



### c)	Least recently used (LRU): 7 fallos de página




|Solicitud | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | 2 | 1 | 3 | 1 |
| -------- | - | - | - | - | - | - | - | - | - | - | - | - |
| Frame 1  | 1#| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Frame 2  |   | 2#| 2 | 2 | 4#| 4 | 4 | 4 | 2#| 2 | 2 | 2 |
| Frame 3  |   |   | 3#| 3 | 3 | 3 | 5#| 5 | 5 | 5 | 3#| 3 | 



#### LRU implementado con stack

|Solicitud                  | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | 2 | 1 | 3 | 1 |
| ------------------------- | - | - | - | - | - | - | - | - | - | - | - | - |
| Más recientemente usado   | 1#| 2#| 3#| 1 | 4#| 1 | 5#| 1 | 2#| 1 | 3#| 1 |
|                           |   | 1 | 2 | 3 | 1 | 4 | 1 | 5 | 1 | 2 | 1 | 3 |
| menos recientemente usado |   |   | 1 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 2 | 2 | 



