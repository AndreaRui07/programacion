import pandas as pd

datos = [10, 20, 30, 40, 50]
serie = pd.Series(datos)
print(serie)

#funcionalidad de pandas

# permite acceder a los datos por indice
# se pueden realizar operaciones matematicas facilmente
# Es mas eficiente que una lista de python cuando se manejan volumenes grandes

print(serie[2])
