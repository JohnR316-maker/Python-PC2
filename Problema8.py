#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento.

#Solución:

numero=int(input("Número:"))
factorial=1
if numero!=0:
 for i in range(1, numero+1):
  factorial=factorial*i
  print("Factorial:", factorial)