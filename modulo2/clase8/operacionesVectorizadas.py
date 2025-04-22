import numpy as np

# Operaciones vectorizadas

arr = np.array([10, 20, 30, 40])
print("array original: ", arr)
print("array sumado 5: ", arr + 5)
print("array multiplicado por 2: ", arr * 2)

# funciones estadisticas

print("suma: ", np.sum(arr))
print("media: ", np.mean(arr))
print("desviacion estandar: ", np.std(arr))
print("maximo: ", np.max(arr))
print("minimo: ", np.min(arr))
