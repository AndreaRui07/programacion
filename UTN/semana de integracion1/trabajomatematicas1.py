numero_decimal = int(input("Ingrese un numero: "))
bits = int(input("Ingrese el numero de bits para la representacion binaria: "))

if numero_decimal < 0:
    numero_binario = bin(2 ** bits + numero_decimal)[2:]
    print(numero_binario.zfill(bits))
else:
    print(bin(numero_decimal)[2:])













