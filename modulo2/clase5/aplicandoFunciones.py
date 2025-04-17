import pandas as pd
dataframe = pd.read_csv("datos.csv")

def categorizar_edad(edad):
    if edad < 30:
        return "joven"
    elif edad < 40:
        return "adulto"
    else:
        return "Mayor"
    
dataframe["categoria edad"] = dataframe["Edad"].apply(categorizar_edad)
print(dataframe)