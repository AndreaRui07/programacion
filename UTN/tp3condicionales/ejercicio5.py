contrasenia = input("ingrese contraseña (entre 8 y 14 caracteres): ")


if 8 <= len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")