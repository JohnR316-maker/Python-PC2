#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.

#Solución

def fib(n):
    a = 0
    b = 1
    for k in range (n):
        c = a + b
        a = b
        b = c
    return b
for x in range(50):
        print(fib(x))