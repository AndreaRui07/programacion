numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

# para asegurar que numero1 sea menor que numero2 siempre

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

suma = 0
for i in range(numero1+1, numero2):
    suma += i
print("La suma de los numeros entre", numero1, "y", numero2, "es: ", suma)
