# Breve Introducción a Python

Esta es una breve (realmente breve!) intro a _Python_ para la materia de Introducción a Sistemas Operativos de la Universidad Nacional de Quilmes.

Durante el transcurso de la materia iremos armando un pequeño emulador de un sistema operativo. Esto nos llevará a tener que modelar los principales componentes de una computadora (CPU, memoria, dispositivos de E/S, etc) sobre los cuales implementaremos los algoritmos que iremos viendo durante la clase. Pero eso es otro tema...

Utilizamos Python por ser un lenguaje rápido para el prototipado, no requiere compilar y posee un __REPL__ (Read Eval Print Loop) muy poderoso que nos permite ir probando a medida que vamos desarrollando.

## Setup

Para comenzar necesitamos tener un entorno con Python funcionando. Todas las distribuciones de _Linux_ tienen una versión de Python instalada ya que es utilizado por muchas de las herramientas del sistema operativo están desarrolladas en Python. Si bien Python se encuentra disponible para diversas plataformas y Sistemas Operativos, recomendamos el uso de un entorno Linux para la materia.

Lo primero que vamos a hacer es probar que nuestro sistema efectivamente tiene Python instalado y que versión. Actualmente hay 2 versiones de Python en uso Python 2 y Python 3. Recientemente se modificado el fin de vida (EOL) de la versión 2 al año 2020, esto se debe a la gran base de librerías y herramientas que aún no han migrado a la versión 3. Nosotros empezaremos directamente con la versión 3, si bien no afecta demasiado lo que haremos.

Veamos que versión de Python tenemos:

```bash
$ python -V
Python 2.7.12
```

Si nos muestra que nuestra versión por defecto de Python es 2.* probemos con:

```bash
$ python3 -V
Python 3.5.2
```

Bien, si vemos algo similar a lo anterior ya estamos listos para empezar. Si no, debemos instalar el paquete que contiene Python 3. Por ejemplo en una distro Ubuntu:

```bash
$ sudo apt-get install python3
```

El instalador para windows esta aca: 

- [Python Windows Installer](https://www.python.org/downloads/windows/)


En general cualquier editor de texto como _Sublime Text_, _Atom_ o _Visual Studio Code_ y una terminal a mano es suficiente para el trabajo que vamos a hacer. Para los amantes de las IDE, existen alternativas como [PyDev](http://www.pydev.org) o [PyCharm CE](https://www.jetbrains.com/pycharm/download/).

## Python Org
  En este site van a poder encontrar mucha información: [Python.org](https://www.python.org/)

Listo, ya tenemos nuestro entorno listo para empezar.

## Introducción al Lenguaje

Para empezar Python es un lenguaje dinámico interpretado (compila a byte-codes). En Python no es necesario declarar el tipo de una variable, parámetros de una función o método. Esto hace el código muy flexible pero con el costo asociado de que perdemos chequeo de tipos en tiempo de compilación.

Python mantiene el tipo de todos los valores en tiempo de ejecución y alerta de errores a medida que ejecuta.

```python
a = 'Hello'
b = ', world!'
print(a + b)   ### imprime 'Hello, world!'

a = 5
print(a + b)   ### ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## Módulos y Archivos de Código

Los archivos código fuente de Python usan la extensión `.py` y son llamados módulos. La forma más fácil de ejecutarlos es desde línea de comando: `python3 hello.py "Sistemas Operativos"`.

El siguiente es un ejemplo de un programa Python. Notar que no utiliza ni llaves ni delimitadores de sentencias. En Python como en Haskell, se utiliza lo que se denomina como _layout rule_ donde la indentación determina donde empieza y termina una sentencia o bloque de código. Por eso es muy importante configurar el editor para que tabule con espacios para no sufrir errores inesperados.

```python
#!/usr/bin/env python3

# acá importamos los módulos que usamos -- sys es un módulo estándar
import sys

# Ponemos nuestro código en una función main()
def main():
    print('Hello there', sys.argv[1])
    # Los argumentos de la líena de comando están en sys.argv[1], sys.argv[2] ...
    # sys.argv[0] es el nombre del propio script como sucede en C

# Código estándar para llamar main() cuando arranca en programa.
if __name__ == '__main__':
    main()
```

En este programa podemos apreciar varias características del lenguaje. Por ejemplo vemos que con `def` estamos definiendo una función. El formato general de una declaración de función es el siguiente:

```python
def func_name(arg):
    body
```

y la invocamos sin el def:

```python
func_name("abc")
```

Una función no debe declarar ni el tipo de los parámetros ni el tipo de retorno. En particular si no se especifica explícitamente el retorno de un valor con `return` por defecto retornará `None` (similar al `null` de C). Adicionalmente una función puede recibir valores por defecto para los argumentos `def repeat(some, times=1)` estos parámetros pueden omitirse en la llamada a la función.

En Python no hay una función `main()` que es el punto de entrada de un programa. Las sentencias más externas de un archivo o módulo Python son ejecutadas en orden una única vez al cargar el módulo de esta forma definiendo funciones y variables. Un módulo Python puede ejecutarse directamente como hicimos anteriormente o hacer un `import` como hicimos con el módulo `sys` en [./hello.py](./hello.py). Cuando lo ejecutamos directamente Python define una variable especial `__name__ = '__main__'`, por eso se usa como convención hacer el `if` verificando si estamos ejecutando el módulo como script o no.

Por último una función es un valor que puede pasarse como parámetro a otra función:

```python
def qsort(arr, comp):
    less = []
    pivot_list = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]

        for elem in arr:
            if comp(elem, pivot) == -1:
                less.append(elem)
            elif comp(elem, pivot) == 1:
                more.append(elem)
            else:
                pivot_list.append(elem)

        less = qsort(less, comp)
        more = qsort(more, comp)

        return less + pivot_list + more

def f(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return 0
```

Cuando importamos un módulo, todas las funciones y variables declaradas están disponibles bajo el namespace con el nombre del módulo salvo que se especifique lo contrario:

```python
import datetime as dt

dt.date.today()

from datetime import *

date.today()
```

## Tipos de Datos

Python provee algunos tipos de datos simples como la mayoría de los lenguajes como booleanos, números y strings. También tipos de datos compuestos como listas, tuplas y diccionarios.

```
# Numbers
int1 = 1
hex1 = 0xDEFABCECBDAECBFBAE
float1 = -32.54e100
complex1 = 3+26j

# Strings
hello = "Hello, world!"

print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
print(hello * 2)
print(hello + "!!!!")

# Lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
list.append(True)
print(list)

# Tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

# Dictionaries
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
```

### Programación Orientada a Objetos

Python es un lenguaje que soporta programación orientada a objetos. Tiene los componentes de otros lenguajes orientados a objetos como Java o Smalltalk con algunas variantes.

Algunos ejemplos:

```python
class Point:
    """
    Represents a 2D math point.
    """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print("Calling")
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def __repr__(self):
        return "Cosa({x},{y})".format(x=self.__x, y=self.__y)

    def __add__(self, point):
        return Point(self.__x + point.x, self.__y + point.y)

class Shape:
    def area():
        raise Exception("Area method not declared")

    def perimeter():
        raise Exception("Perimeter method not declared")

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return self._length * 2 + self._width * 2

    def __repr__(self):
        return "Rectangle({length}, {width})".format(length=self._length, width=self._width)

class Circle(Shape):
    pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return Circle.pi * (self._radius ^ 2)

    def perimeter(self):
        return 2 * Circle.pi * self._radius

    def __repr__(self):
        return "Circle({radius})".format(radius=self._radius)
```

## Estructuras de Control

Como todo lenguaje imperativo, Python provee las estructuras de control de flujo tradicionales como `if`, `for`, `while`, `repeat`, etc.

El `if` es similar al de cualquier lenguaje, ejecuta código de forma condicional evaluando un expresión booleana. Adicionalmente agrega la cláusula `elif` que permite encadenar varios expresiones condicionales. Particularmente Python no soporta las sentencias `case` o `switch` encontradas en otros lenguajes, la forma de hacer algo similar es mediante sentencias `if/elif/else`

```python
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

El `if` también puede utilizarse en forma inline como una expresión de la siguiente forma:

```python
res = -1 if x < 0 else 1
```

En Python la sentencia for itera sobre una secuencia a diferencia de C por ejemplo.

```python
words = ['cat', 'dog', 'bird']

for word in words:
    print(word)
```

