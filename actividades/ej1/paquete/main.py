from carrito_paquete.productos import obtener_productos
from carrito_paquete.menu import iniciar_menu


def main():
    productos = obtener_productos()
    carrito = []
    print("=== CARRITO DE COMPRAS ===")
    iniciar_menu(productos, carrito)


main()
