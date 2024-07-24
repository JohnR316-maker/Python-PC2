#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.

#Solución

texto = input("introduzca el texto").lower()
vocales = ('a', 'e', 'i', 'o', 'u') 
for letra in vocales:
       texto = texto.replace(letra, " ")