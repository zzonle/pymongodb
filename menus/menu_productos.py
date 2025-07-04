from colorama import init, Fore, Style
from colecciones.productos import *
init(autoreset=True)

def menu_productos(db):
    while True:
        ancho = 40
        print(Fore.CYAN + "=" * ancho)
        print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ PRODUCTOS")
        print(Fore.CYAN + "=" * ancho)
        print(Fore.GREEN + "1. Leer producto")
        print(Fore.GREEN + "2. Leer producto por id")
        print(Fore.GREEN + "3. Agregar producto")
        print(Fore.GREEN + "4. Agregar varios productos")
        print(Fore.GREEN + "5. Actualizar producto")
        print(Fore.GREEN + "6. Eliminar producto")
        print(Fore.RED + "q. Volver menú principal")
        print(Fore.CYAN + "=" * ancho)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_productos(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion == "2":
            leer_productos_por_id(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion == "3":
            agregar_producto(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion == "4":
            agregar_varios_productos(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion == "5":
            actualizar_producto(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion == "6":
            eliminar_producto(db)
            input("Presione ENTER para volver al menú de productos...")
        elif opcion.lower() == "q":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

