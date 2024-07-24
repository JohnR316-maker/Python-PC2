#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.

Nuevo_diccionario = {}
Dato_Alumno1 = {"Nombre": "Roberto Palacios", "Nota1": 16, "Nota2": 18, "Nota3":19}
Dato_Alumno2 = {"Nombre": "Javier Mejia", "Nota1": 15, "Nota2": 20, "Nota3":16}
type(Nuevo_diccionario)
print(Dato_Alumno1["Nombre"])
print(Dato_Alumno2.get("Nota1"))
