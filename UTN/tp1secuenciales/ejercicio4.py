# crear un programa que solicite el radio de un circulo e imprima por pantalla su area y su perimetro

radio = int(input("Ingrese el radio de un circulo: "))

pi = 3.14159

area = pi * radio * radio
perimetro = 2 * pi * radio

print(f"El area del circulo es:{area} y su perimetro es:{perimetro}")