import numpy as np

#ejercico 1: crear un array del 1 al 10

ejercicio1 = np.array([1,2,3,4,5,6,7,8,9,10])

#Ejercicio 2: acceder al primer elemento
ejercicio2 = ejercicio1[0] #dentro del [] la posicion del elemento
print(ejercicio2)

# ejercicio 3: acceder al ultimo elemento
# suponiendo que no se cual es su ultimo elemento

ejercicio3 = ejercicio1[-1] #con el -1 accedo al ultimo elemento
print(ejercicio3)

# mostrar del segundo al quinto elemento
# aca usamos el slicing
ejercicio4 = ejercicio1[1:4] #el 1 muestra el orden y desp de los : muestra el elemento
print(ejercicio4)
