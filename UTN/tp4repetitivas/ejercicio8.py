
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0 


for i in range(0,100):
   
    i = int(input("ingrese un numero: "))
    
    if i % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

    if i > 0:
        cont_positivos += 1
    elif i < 0:
        cont_negativos += 1 

print("Resultados:")
print("La cantidad de numeros pares es:", cont_pares)
print("La cantidad de numeros impares es:", cont_impares)
print("La cantidad de numeros positivos es:", cont_positivos)
print("La cantidad de numeros negativos es:", cont_negativos)