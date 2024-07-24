#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números. Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.

#Solución:
n = 1
par = impar = 0
while n != 0:
    n = int(input("Ingresa un número: "))
    if n > 0:
        if n % 2 == 0:
         par += 1
        else:
         impar += 1
print("El total de números pares es: ", par)
print("El total de números impares es: ", impar)