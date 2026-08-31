from carrito_paquete.carrito import agregar_producto, mostrar_carrito, vaciar_carrito
from carrito_paquete.pagos import total_pagar, generar_factura
from carrito_paquete.productos import mostrar_productos


def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Mostrar productos")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Ver total")
    print("5. Generar factura")
    print("6. Vaciar carrito")
    print("7. Salir")


def ejecutar_opcion(opcion, productos, carrito):
    if opcion == "1":
        mostrar_productos(productos)
    elif opcion == "2":
        mostrar_productos(productos)
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        agregar_producto(carrito, productos, nombre, cantidad)
    elif opcion == "3":
        mostrar_carrito(carrito)
    elif opcion == "4":
        print("Total a pagar: S/", total_pagar(carrito, productos))
    elif opcion == "5":
        cliente = input("Nombre del cliente: ")
        generar_factura(carrito, productos, cliente)
    elif opcion == "6":
        vaciar_carrito(carrito)
    elif opcion == "7":
        print("Gracias por su compra.")
        return False
    else:
        print("Opción no válida. Intente nuevamente.")
    return True


def iniciar_menu(productos, carrito):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not ejecutar_opcion(opcion, productos, carrito):
            break
