from colorama import init, Fore, Style
from colecciones.pedidos import *
init(autoreset=True)

def menu_pedidos(db):
    while True:
        ancho = 40
        print(Fore.CYAN + "=" * ancho)
        print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ PEDIDOS")
        print(Fore.CYAN + "=" * ancho)
        print(Fore.GREEN + "1. Leer pedido")
        print(Fore.GREEN + "2. Leer pedido por id")
        print(Fore.GREEN + "3. Agregar pedido")
        print(Fore.GREEN + "4. Actualizar pedido")
        print(Fore.GREEN + "5. Eliminar pedido")
        print(Fore.RED + "q. Volver menú principal")
        print(Fore.CYAN + "=" * ancho)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_pedidos(db)
            input("Presione ENTER para volver al menú de pedidos...")
        elif opcion == "2":
            leer_pedidos_por_id(db)
            input("Presione ENTER para volver al menú de pedidos...")
        elif opcion == "3":
            agregar_pedido(db)
            input("Presione ENTER para volver al menú de pedidos...")
        elif opcion == "4":
            actualizar_pedido(db)
            input("Presione ENTER para volver al menú de pedidos...")
        elif opcion == "5":
            eliminar_pedido(db)
            input("Presione ENTER para volver al menú de pedidos...")
        elif opcion.lower() == "q":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
