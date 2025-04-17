import pandas as pd

empleados ={
    "Nombre": ["Carlos", "Ana", "Pedro", "Lucia", "Juan", "sofia", "Diego","Mariana", "Fernando", "Laura", "Martin", "Valentina", "Andres", "Gabriela", "Luis", "Patricia", "Ricardo", "Cecilia", "Javier", "Monica", "Hugo", "Silvia", "Roberto", "Paula", "Gustavo", "Elena", "Alberto", "Veronica", "Sergio", "Camila", "Esteban", "Rocio", "Matias", "Carla", "Daniel", "Florencia", "Oscar", "Daniela", "Emilia", "Noelia", "Manuel", "Victoria", "Tomas", "Julieta", "Raul", "Bianca", "Eduardo", "Agustina", "Facundo","Celeste"],
    "Edad": [42, 53, 34, 36, 44, 36, 38, 40, 52, 59, 33, 32, 26, 60, 34, 43, 55, 54, 43, 47, 40, 56, 26, 54, 53, 53, 53, 46, 45, 58, 52, 57, 37, 32, 60, 42, 46, 32, 42, 51, 57, 58, 25, 53, 35, 34, 45, 55, 41, 35],
    "Salario": [7533, 5810, 5798, 4100, 5862, 3519, 7537, 6246, 5061, 5011, 5825, 6679, 6709, 3573, 6733, 6756, 5839, 4018, 5947, 7658, 6766, 7918, 5013, 4343, 4658, 4764, 6760, 6389, 3187, 6394, 7834, 3441, 4979, 6563, 7327, 5583, 5410, 6420, 3838, 4387, 7880, 7793, 3181, 3321, 3930, 5221, 7005, 4995, 5029, 5361],
    "Ciudad": ["Salta", "La Plata", "Rosario", "Rosario", "Salta", "Cordoba", "Mendoza", "Rosario", "Buenos Aires", "Cordoba", "Salta", "Rosario", "Salta", "Salta", "Rosario", "La Plata", "Mendoza", "Mendoza", "Rosario", "La Plata", "Mendoza", "Mendoza", "Salta", "Buenos Aires", "Mendoza", "Salta", "Rosario", "Cordoba", "Rosario", "La Plata", "Cordoba", "La Plata", "Mendoza", "Cordoba", "Mendoza", "Rosario", "Cordoba", "La Plata", "La Plata", "La Plata", "Mendoza", "La Plata", "Cordoba", "Cordoba", "Salta", "Cordoba", "Salta", "Buenos Aires", "Rosario", "Rosario"],
    "bonos": [585, 547, 906, 1470, 651, 1190, 1767, 1498, 1703, 1392, 1398, 1049, 1755, 1051, 1548, 1549, 1467, 1692, 1014, 768, 1226, 1357, 632, 695, 1284, 588, 1175, 1006, 1807, 1778, 1017, 1895, 520, 722, 1317, 1880, 1772, 584, 1993, 662, 1157, 1270, 642, 1691, 1904, 1019, 1527, 960, 1919, 701]
}
dataframe = pd.DataFrame(empleados)

dataframe.to_csv("empleados.csv", index=False)