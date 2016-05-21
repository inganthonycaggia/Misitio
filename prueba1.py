
import math
opc = 's'

while opc == 's':

 operacion = raw_input('Bienvenido al menu de la primera prueba\n Que desea realizar: \n 1. Calcular longitud.\n 2. Calcular raiz cuadrada ')
 if operacion == '1':
  palabra = raw_input('Ingrese una palabra: ')
  print 'esta palabra tiene una cantidad de: '
  print  len(palabra)

 elif operacion == '2':

  num = input('Ingrese Numero: ')
  raiz = math.sqrt(num)
  print 'La raiz cuadradra de este numero es: '
  print raiz

 opc = raw_input('Desea continuar: (S/N): ')
 if opc == 'n':
 	print ('gracias por usar mi programa *hasta la proxima*') 