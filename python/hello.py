#!/usr/bin/env python

# acá importamos los módulos que usamos -- sys es un módulo estándar
import sys

# Ponemos nuestro código en una función main()
def main():
    print('Hello there', sys.argv[1])
    # Los argumentos de la líena de comando están en sys.argv[1], sys.argv[2] ...
    # sys.argv[0] es el nombre del propio script como sucede en C.

# Código estándar para llamar main() cuando arranxca en programa.
if __name__ == '__main__':
    main()
