from carrito_paquete.carrito import mostrar_carrito


def total_pagar(carrito, productos):
    total = 0
    for producto, cantidad in carrito:
        total = total + productos[producto] * cantidad
    return total


def generar_factura(carrito, productos, cliente):
    print("--- FACTURA ---")
    print("Cliente:", cliente)
    mostrar_carrito(carrito)
    print("Total a pagar: S/", total_pagar(carrito, productos))
