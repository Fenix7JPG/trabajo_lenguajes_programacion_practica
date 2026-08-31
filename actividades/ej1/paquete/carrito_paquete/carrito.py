def agregar_producto(carrito, productos, nombre, cantidad):
    nombre = nombre.lower()
    if nombre in productos:
        carrito.append((nombre, cantidad))
        print("Producto agregado al carrito.")
    else:
        print("Ese producto no existe.")


def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("--- CARRITO ---")
        for producto, cantidad in carrito:
            print(producto, "x", cantidad)


def vaciar_carrito(carrito):
    carrito.clear()
    print("El carrito fue vaciado.")
