num = int(input("ingrese un numero: "))
suma = 0

while  num != 0:
    suma += num
    print(suma)
    num = int(input("ingrese un numero: "))
    
print("El total acumulado es", suma)
