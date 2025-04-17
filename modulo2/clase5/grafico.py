import pandas as pd
import matplotlib.pyplot as plt

empleados = pd.read_csv("empleados.csv")

# definir el tamaño del grafico
plt.figure(figsize= (10,5)) # va a tener 10 de ancho por 5 de alto (pulgadas)

# creamos el grafico de barras

plt.bar(empleados["Nombre"], empleados["Salario"], color="skyblue")

""" 
plt.bar(): Genera un gráfico de barras.

df["Nombre"]: Define los valores en el eje X (nombre de los empleados).

df["Salario"]: Define los valores en el eje Y (salario de cada empleado).

color="skyblue": Cambia el color de las barras a azul claro.
 """
# agregar etiqueta a los ejes y el titulo

plt.xlabel("empleado") #etiqueta eje x
plt.ylabel("salario") # etiqueta eje y
plt.title("salario de cada empleado") # titulo del grafico

# ajustando la rotacion de los nombres
plt.xticks(rotation=45)
plt.show()
