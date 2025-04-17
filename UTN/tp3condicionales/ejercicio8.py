nombre = input("Ingrese su Nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 si quiere su nombre en mayúsculas, en minúsculas o con la primera letra mayúscula: "))
               
if opcion == 1:
    print(nombre.upper())   
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no valida")