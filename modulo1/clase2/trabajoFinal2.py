""" 
crear un programa que almacene informacion sobre productos en un inventario y permita consultad detalles de su codigo

 """
inventario = {
    "B202": {"nombre": "mouse", "precio": 25, "stock": 20},
    "C303": {"nombre": "teclado", "precio": 45, "stock": 15},
    "A101": {"nombre": "Laptop", "precio": 800, "stock": 5}}
codigo = input("Ingrese el codigo del producto: ")

if codigo in inventario:
    producto = inventario[codigo]
    print(f"nombre:{producto['nombre']}")
    print(f"precio:{producto['precio']}")
    print(f"stock:{producto['stock']}")
else:
    print("producto no encontrado")

