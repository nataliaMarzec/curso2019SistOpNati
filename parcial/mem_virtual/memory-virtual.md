# Administración de Memoria: Memoria Virtual
## práctica: algoritmos de selección de víctima


Una computadora tiene 4 marcos. El tiempo de carga, tiempo de Último acceso, y los bits de Referencia y
Modicación para cada página se muestran a continuación (los tiempos están ticks del reloj):



| Página | T Carga | Última Referencia | R  |  M | 
| -------| ------- | ----------------- | -- | -- |
|   0    |  240    |       260         |  1 |  1 |
|   1    |  230    |       235         |  1 |  1 |
|   2    |  230    |       270         |  1 |  0 |
|   3    |  140    |       350         |  0 |  0 |




a) Qué página reemplaza FIFO?

b) Qué página reemplaza LRU?

c) Qué página reemplaza el algoritmo de segunda oportunidad?
> Considerar que la “aguja” esta en la página 0 



## Solución: 


|  Algoritmo   | Página | 
| ------------ | -----  |
| a) FIFO      |   3    | 
| b) LRU       |   1    |
| c) 2nd Chance|   3    |



### a) FIFO :  	Pág 3


| Página | **T Carga** | Última Referencia | R  |  M |
| -------| ------- | ----------------- | -- | -- |
|   0    |  240    |       260         |  1 |  1 |
|   1    |  230    |       235         |  1 |  1 |
|   2    |  230    |       270         |  1 |  0 |
|  **3** | **140** |       350         |  0 |  0 |


### b)	Least recently used (LRU):  Pág 1


| Página | T Carga | **Última Referencia** | R  |  M |
| -------| ------- | ----------------- | -- | -- |
|   0    |  240    |       260         |  1 |  1 |
|  **1** |  230    |     **235**       |  1 |  1 |
|   2    |  230    |       270         |  1 |  0 |
|   3    |  140    |       350         |  0 |  0 |

### c)	Clock Second Chance:  Pág 3



| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | --     | -- | --------- |
|   0    |  240    |       260         |  1     |  1 | <--       |
|   1    |  230    |       235         |  1     |  1 |           |
|   2    |  230    |       270         |  1     |  0 |           |
|   3    |  140    |       350         |  0     |  0 |           |



 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 0)

| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | --     | -- | --------- |
|   0    |  240    |       260         |  **0** |  1 |           |
|   1    |  230    |       235         |  1     |  1 | <--       |
|   2    |  230    |       270         |  1     |  0 |           |
|   3    |  140    |       350         |  0     |  0 |           |


 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 1)

| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | --     | -- | --------- |
|   0    |  240    |       260         |  0     |  1 |           |
|   1    |  230    |       235         |  **0** |  1 |           |
|   2    |  230    |       270         |  1     |  0 | <--       |
|   3    |  140    |       350         |  0     |  0 |           |


 luego de mover la "aguja" y limpiar el bit de R (segunda chance para Pág 2)

| Página | T Carga | Última Referencia | **R**  |  M | **Aguja** | 
| -------| ------- | ----------------- | --     | -- | --------- |
|   0    |  240    |       260         |  0     |  1 |           |
|   1    |  230    |       235         |  0     |  1 |           |
|   2    |  230    |       270         |  **0** |  0 |           |
|   **3**|  140    |       350         |  0     |  0 | **<--**       |

 la "aguja" apunta a una Página con bit R = 0  (Víctima = Página 3)






