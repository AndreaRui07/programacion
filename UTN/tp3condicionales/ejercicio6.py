import random
from statistics import multimode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mi_lista = numeros_aleatorios

media = mean(mi_lista)
mediana = median(mi_lista)
modas = multimode(mi_lista)
moda = modas[0]

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar sesgo claro")

print(f"La lista obtenida es: ", mi_lista, "Media: ", media, ", Mediana: ", mediana, ", Moda: ", moda)