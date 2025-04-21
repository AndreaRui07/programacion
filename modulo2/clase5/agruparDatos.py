import pandas as pd
dataframe = pd.read_csv("datos.csv")

# como agrupar datos. Agrupar por ciudad y sacar salario promedio

df_agrupado = dataframe.groupby("Ciudad")["Salario"].mean()
print(df_agrupado)

# .groupby() agrupa elementos