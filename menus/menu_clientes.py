from colorama import init, Fore, Style
from colecciones.clientes import *
init(autoreset=True)

def menu_clientes(db):
    while True:
        ancho = 40
        print(Fore.CYAN + "=" * ancho)
        print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ CLIENTES")
        print(Fore.CYAN + "=" * ancho)
        print(Fore.GREEN + "1. Leer cliente")
        print(Fore.GREEN + "2. Leer cliente por id")
        print(Fore.GREEN + "3. Agregar cliente")
        print(Fore.GREEN + "4. Agregar varios clientes")
        print(Fore.GREEN + "5. Actualizar cliente")
        print(Fore.GREEN + "6. Eliminar cliente")
        print(Fore.RED + "q. Volver menú principal")
        print(Fore.CYAN + "=" * ancho)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_clientes(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion == "2":
            leer_clientes_por_id(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion == "3":
            agregar_cliente(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion == "4":
            agregar_varios_clientes(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion == "5":
            actualizar_cliente(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion == "6":
            eliminar_cliente(db)
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion.lower() == "q":
            break
        else:
            print("Opción no válida. Intente de nuevo.")




    

    