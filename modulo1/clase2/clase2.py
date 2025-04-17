#tipos de variables

entero= 20  #variable del tipo integer (entero)
decimal= 0.5 #variable del tipo float (decimal)
string = "hola" #variable de tipo string (cadena, caracter)
booleano = "true" 
#variable de tipo bool, admite solo valores true or false
#para cambiar de carpeta en la terminal colocar cd NOMBRE_CARPETA
#si queres volver para atras, ejecutamos: cd..
print(string)

print((36 % 3 ==0))

#if-else (condicionales)
edad = int(input("ingrese su edad: ")) #int convierte en entero el input ingresado

if edad >= 18:
    print("el usuario es mayor de edad")
else:
    print("el usuario es menor de edad")
