magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve.(Imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve. (Ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado. (Sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte. (puede causar daños en estructuras debiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print( "Extremo. (puede causar graves daños a gran escala)")
else:
    print("Dato invalido")
