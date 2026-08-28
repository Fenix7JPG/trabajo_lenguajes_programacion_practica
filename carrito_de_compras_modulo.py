def añadir_carrito(carrito,producto,cantidad,productos):
    if producto in productos:
        carrito.append((producto,cantidad))
        print("Producto agregado al carrito.")
    else:
        print("Ese producto no existe.")

def total_pagar(carrito,productos):
    total=0
    for producto,cantidad in carrito:
        total+=productos[producto]*cantidad
    return total

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Carrito:")
        for producto,cantidad in carrito:
            print(f"{producto}:{cantidad}")

def factura(carrito,cliente="Cliente general",productos=None):
    print("Factura:")
    print("Cliente:",cliente)
    mostrar_carrito(carrito)
    total=total_pagar(carrito,productos)
    print("Total a pagar:",total)

def menu(productos,carrito):
    while True:
        print("---MENÚ---")
        print("1.Agregar producto")
        print("2.Mostrar carrito")
        print("3.Ver total")
        print("4.Generar factura")
        print("5.Salir")
        opcion=input("¿Qué quieres hacer? ")
        if opcion=="1":
            print("Productos disponibles:")
            print(productos)
            producto=input("¿Qué producto quieres? ").lower()
            cantidad=int(input("¿Cuántos quieres? "))
            añadir_carrito(carrito,producto,cantidad,productos)
        elif opcion=="2":
            mostrar_carrito(carrito)
        elif opcion=="3":
            print("Total a pagar:",total_pagar(carrito,productos))
        elif opcion=="4":
            cliente=input("Nombre del cliente: ")
            factura(carrito,cliente,productos)
        elif opcion=="5":
            print("Gracias por comprar.")
            break
        else:
            print("Opción no válida.")