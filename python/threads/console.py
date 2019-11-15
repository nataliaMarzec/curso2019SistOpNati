# Exemplo de construccion de una Consola simple en python

def process_input(command_line):
  print(' processing command: '+command_line)




# la función main() hace un loop leyendo los comandos del usuario hasta que se ingrese el comando 'exit'
def start_console():
  running = True

  while running:
    command_line = input("$ ")
    if command_line == 'exit':
      running = False
    else:  
      process_input(command_line)



# Código estándar para llamar main() cuando arranxca en programa.
if __name__ == '__main__':
    start_console()



