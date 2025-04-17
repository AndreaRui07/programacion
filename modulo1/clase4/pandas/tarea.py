import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos"],
    "Edad": [25, 30, 35, 40, 50],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman"],
    "Salario": [3000, 4000, 5000, 6000, 7000]})

print(df)

# ejercicio 2

print(df["nombre"])

print(df["Salario"])

# ejercicio 3

mayores_30 = df[df["Edad"] > 30]
print(mayores_30)

salario_mayor_4000 = df[df["Salario"] > 4000]
print(salario_mayor_4000)
