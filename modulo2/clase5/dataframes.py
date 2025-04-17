import pandas as pd

#Datos para diccionario
datos = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos"],
    "Edad": [25,30,35,40,45],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman"],
    "Salario": [3000, 4000, 5000, 6000, 7000]
}

df = pd.DataFrame(datos)

print(df)

datos2 ={
    "Nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos", "Sofia", "Diego", "Mariana", "Luis", "Valeria", "Fernando", "Gabriela", "Ricardo", "Camila", "Andres"],
    "Edad": [25, 30, 35, 40, 45, 28, 33, 38, 43, 48, 27, 32, 37, 42, 47],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman", "Salta", "Santa Fe", "Mar del Plata", "Neuquen", "San Luis", "La Plata", "Bahia Blanca", "San Juan", "Jujuy", "Chaco"],
    "Salario": [3000, 4000, 5000, 6000, 7000, 3500, 4500, 5500, 6500, 7500, 3200, 4200, 5200, 6200, 7200]
}
dataframe = pd.DataFrame(datos2)
 # Metodos utiles de dataframes

print(dataframe.head())  # .head muestra las primer 5 entradas
print(dataframe.tail())  # .tail muestra las ultimas 5 entradas
print(dataframe.shape) # .shape muestra la cantidad de filas y columnas
print(dataframe.info()) # muestra datos del dataframe como uso de memoria

# para acceder a una columna

print(dataframe["Nombre"])

# para acceder a una fila

print(dataframe.iloc[2])

# datos estadisticos

print(dataframe.describe()) # estadisticas generales para columnas numericas
