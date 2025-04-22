import numpy as np
# usando listas de python
lista = [1, 2, 3, 4, 5]
resultado_lista = [x * 2 for x in lista] #multiplica cada elemento de 
# la lista por 2

# usando numpy
arr = np.array([1, 2, 3, 4, 5]) # el array es = lista
resultado_np = arr * 2 # multiplica array x 2

print(resultado_lista)
print(resultado_np)