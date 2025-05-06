numero = int(input("Ingresa un número: "))
numero_invertido = 0

# Detectar si el número es negativo
es_negativo = False
if numero < 0:
    es_negativo = True
    # Toma el valor absoluto (abs(numero)) para trabajar con él
    numero = abs(numero)

# Invertir los dígitos usando un ciclo
while numero != 0:
    # % 10: obtiene el último dígito del número
    digito = numero % 10
    # * 10 + dígito: va armando el número al revés
    numero_invertido = numero_invertido * 10 + digito
    # // 10: elimina el último dígito del número
    numero = numero // 10

# Aplicar el signo si era negativo
if es_negativo:
    numero_invertido = -numero_invertido

print("Número invertido:", numero_invertido)
