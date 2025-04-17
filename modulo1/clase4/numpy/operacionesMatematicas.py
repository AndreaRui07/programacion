import numpy as np

arr = np.array([1,2,3,4,5,])
print(arr + 10) # suma 10 a cada elemento dentro del array
print(arr * 2) # multiplica cada elemento del array por 2
print(arr ** 2) # saca el cuadrado de cada elemento del array
print(np.sqrt(arr)) # raiz cuadrada

# calcula la suma total y el promedio de un  array [4,8,12,16]

ejercicio1 = np.array([4,8,12,16])

suma_total = np.sum(ejercicio1) #suma los elementos del array
promedio = np.mean(ejercicio1) # hace el promedio de los elementos del array
print(suma_total)
print(promedio)
