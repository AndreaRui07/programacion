import pandas as pd

dataframe_nuevo = pd.read_csv("datos.csv")
print(dataframe_nuevo)

 # ordenar dataframe. puede ser por edad, salario,etc

dataframe_ordenado = dataframe_nuevo.sort_values("Edad")
print(dataframe_ordenado)

# ordenar los datos de manera descendente por edad

df_descendente = dataframe_nuevo.sort_values("Edad", ascending=False)
print(df_descendente)
 # comor ordenar los salarios de mayor a menor

df_salario_descendente = dataframe_nuevo.sort_values("Salario", ascending=False)
print(df_salario_descendente)

# ordenar nombres alfabeticamente

df_nombres_alfabetico = dataframe_nuevo.sort_values(by="Nombre")
print(df_nombres_alfabetico)