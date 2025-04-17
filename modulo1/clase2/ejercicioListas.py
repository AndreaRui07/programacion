ciudades = ["azul","tandil,", "Olavarria","tapalque","Alvear"]

#para agregar elementos a la lista usamos .append

ciudades.append("Juarez")

print(ciudades)

# para eliminar elementos de la lista usamos .remove

ciudades.remove("Olavarria")

print(ciudades)

print(ciudades[3])


indiceAzul = ciudades.index("azul")

print(indiceAzul)
print(ciudades[indiceAzul])