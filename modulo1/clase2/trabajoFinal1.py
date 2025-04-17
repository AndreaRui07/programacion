""" crear un programa que almacene una lista de estudiantes en un diccionario y permita consultar datos

 """
# diccionario dentro de un diccionario
estudiantes = {
    "001": {"nombre": "Juan", "apellido": "Perez", "curso": "python"},
    "002" : {"nombre": "Pedro", "Apellido": "Gomez", "curso": "Javascript"}}

# lista de diccionarios
EstudantesListas = [{"nombre": "Juan", "apellido": "Perez", "curso": "python"},{"nombre": "Pedro", "Apellido": "Gomez", "curso": "Javascript"}]

codigo = input("ingrese el id del estudiante: ")

"""
iteracion es una forma de recorrer o repetir un comando, especialmente utiles en estructura de datos

 """
if codigo in estudiantes:
    print(estudiantes[codigo])
else:
    print("estudiante no encontrado")
