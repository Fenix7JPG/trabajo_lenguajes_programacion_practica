def obtener_productos():
    productos = {
        "pan": 1.50,
        "leche": 4.00,
        "arroz": 5.00,
        "huevos": 8.00,
        "gaseosa": 3.50
    }
    return productos


def mostrar_productos(productos):
    print("--- PRODUCTOS DISPONIBLES ---")
    for nombre in productos:
        print(nombre, "- S/", productos[nombre])
