def mostrar_menu():
    print("=== MENÚ DE OPCIONES ===")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Salir")
    print("========================")


def ejecutar_opcion(opcion):
    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        opcion_4()
    elif opcion == "5":
        return False
    else:
        print("Opción no válida. Intente nuevamente.")
    return True


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not ejecutar_opcion(opcion):
            print("Saliendo del programa...")
            break


def opcion_1():
    print("Has seleccionado la Opción 1")


def opcion_2():
    print("Has seleccionado la Opción 2")


def opcion_3():
    print("Has seleccionado la Opción 3")


def opcion_4():
    print("Has seleccionado la Opción 4")