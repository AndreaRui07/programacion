import pandas as pd
empleados = pd.read_csv("empleados.csv")
print(empleados)

print(empleados.info())
print(empleados.describe()) #muestra los datos estadisticos 

Salarios_Altos = empleados[empleados["Salario"] > 5000] #filtra los salarios mayores a 5000

print(Salarios_Altos)

Edades_descendentes = empleados.sort_values("Edad", ascending=False)
print(Edades_descendentes)

# agrupar por ciudades y sacar promedio del salario

empleados_agrupados = empleados.groupby("Ciudad")["Salario"].mean()
print(empleados_agrupados)

# categorizacion por edades

def categorizar_edad(edad):
    if edad < 30:
        return "joven"
    elif edad < 40:
        return "Adulto"
    else:
        return "Mayor"
    
empleados["categoria edad"] = empleados["Edad"].apply(categorizar_edad)
print(empleados)