# Administración de Memoria: Memoria Virtual
## práctica: algoritmos de selección de víctima


Una computadora tiene 4 marcos. El tiempo de carga, tiempo de Último acceso, los bits de Referencia y
Modicación y la "Aguja"  para cada página se muestran a continuación (los tiempos están ticks del reloj):


a) Qué página reemplaza FIFO?

b) Qué página reemplaza LRU?

c) Qué página reemplaza el algoritmo de segunda oportunidad?
  > Considerar que la “aguja” esta en la página 2



## Ejercicio 1: 

| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  150    |       325         |  1 |  1 |       | 
|   1    |  245    |       245         |  0 |  1 | <--   |
|   2    |  220    |       220         |  1 |  0 |       |
|   3    |  100    |       350         |  0 |  0 |       |

- [Resultados del Ejercicio 1](./practica_memory-virtual_result_1.md)



## Ejercicio 2: 

| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  110    |       350         |  0 |  1 |       | 
|   1    |  120    |       320         |  0 |  1 |       |
|   2    |  130    |       310         |  0 |  0 |       |
|   3    |  140    |       300         |  1 |  0 | <--   |

- [Resultados del Ejercicio 2](./practica_memory-virtual_result_2.md)



## Ejercicio 3: 


| Página | T Carga | Última Referencia | R  |  M | Aguja | 
| -------| ------- | ----------------- | -- | -- | ----- |
|   0    |  200    |       245         |  1 |  0 |       | 
|   1    |  201    |       210         |  1 |  1 |       |
|   2    |  185    |       233         |  1 |  0 |       |
|   3    |  220    |       230         |  1 |  1 | <--   |

- [Resultados del Ejercicio 3](./practica_memory-virtual_result_3.md)