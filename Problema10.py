#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
#la lista abajo:

fecha = input("Introduce la fecha en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mes = mesaño[:mesaño.find('/')]
print('Mes', mes)
