""" 
Es una estructura de datos que se caracteriza por tener pares clave-valor

ejemplo: persona = {"nombre": "Andrea", "Edad": 45, "ciudad": "Azul"}
Son mutables

 """

persona = {"nombre": "Andrea", "edad": 45, "ciudad": "Azul"}

print(persona["nombre"])

# como modificar un valor del diccionario

persona["nombre"] = "Marcela"

print(persona)

# agregar un nuevo valor

persona["profesion"] = "comerciante"
print(persona)

# metodos practicos y utiles de diccionarios
# metodo keys- muestra listas de claves

print(persona.keys())

#metodo values- muestra lista de valores

print(persona.values())