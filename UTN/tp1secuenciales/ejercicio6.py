#pedir un numero al usuario e imprimir su tabla de multiplicar

numero = int(input("Ingrese un numero: "))

for i in range (0,11):
    resultado = numero * i
    print(resultado)