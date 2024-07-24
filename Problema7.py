#Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
#perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
#(excluyendo el propio número).

#Solución

for n in range(1,1001):
     i = 2
     suma = 0
     while i <= n:
        if n % i == 0:
            suma += n // i
        i += 1
     if suma == n:
         print(n)