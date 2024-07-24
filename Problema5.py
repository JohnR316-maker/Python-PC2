#Escribe un programa que encuentre la suma de todos los números primos menores que 100

#Solución

def criba_eratostenes(n):
    primos = []
    no_primos = []
    for i in range(2, n + 1):
        if i not in no_primos:
            primos.append(i)

            for j in range(i * i, n + 1, i):
                no_primos.append(j)
    
    return primos

print(criba_eratostenes(100))
print(len(criba_eratostenes(100)))