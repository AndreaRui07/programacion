import pandas as pd

# los data frame son diccionarios que se parecen a una tabla de excel, a una base de datos. 
# tienen filas. cada fila representa un registro
# lleva llave {} adentro

df = pd.DataFrame({
    "nombre": ["ana", "juan", "Pedro"],
    "edad": [25, 30, 35],
    "salario": [3000, 4000, 5000]
})
print(df)

# filtro en df a las personas mayores de 30

mayores_30 = df[df["edad"] > 30]
print(mayores_30)

# para filtrar solo los nombres de df

print(df["nombre"])

# para filtrar solo los salarios
print(df["salario"])

# para acceder a una fila especifica

print(df.iloc[2])

# como modificar algun dato en el df

df["salario"] = df["salario"] * 1.2  # 1.2 indica un aumento del 20 %

print(df["salario"])

print(df)