import random

numero = random.randint(0,9)
intentos = 0
adivinar_numero = int(input("Adivina el numero (entre 0 y 9): "))
while adivinar_numero != numero:
    intentos += 1
    print("Incorrecto! Intenta nuevamente: ")
    adivinar_numero =int(input("Adivina el numero (entre 0 y 9): "))
   
intentos +=1
print("Correcto! Adivinaste en", intentos, "intento(s)")