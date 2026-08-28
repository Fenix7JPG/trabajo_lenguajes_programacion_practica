def añadir_carrito(carrito,producto,cantidad,productos):
    if producto in productos:
        carrito.append((producto,cantidad))
        print("Producto agregado al carrito.")
    else:
        print("Ese producto no existe.")

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Carrito:")
        for producto,cantidad in carrito:
            print(f"{producto}:{cantidad}")