from carrito import *

def total_pagar(carrito,productos):
    total=0
    for producto,cantidad in carrito:
        total+=productos[producto]*cantidad
    return total

def factura(carrito,cliente="Cliente general",productos=None):
    print("Factura:")
    print("Cliente:",cliente)
    mostrar_carrito(carrito)
    total=total_pagar(carrito,productos)
    print("Total a pagar:",total)