
def determinar_estacion(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "invierno" 
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "primavera"  # Ajuste para hemisferio norte, sería "Primavera" en hemisferio sur
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Verano"  # Ajuste para hemisferio norte, sería "Invierno" en hemisferio sur
    else:
        return "otoño"  # Ajuste para hemisferio norte, sería "Otoño" en hemisferio sur

def determinar_estacion_hemisferio_sur(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
hemisferio = input("Ingrese el hemisferio (Norte/Sur): ")
    
if hemisferio.lower() == "norte":
        estacion = determinar_estacion(dia, mes)
        print(f"La estación es: {estacion}")
elif hemisferio.lower() == "sur":
        estacion = determinar_estacion_hemisferio_sur(dia, mes)
        print(f"La estación es: {estacion}")
else:
        print("Hemisferio no reconocido.")


