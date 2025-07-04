from menus.menu_clientes import menu_clientes 
from menus.menu_pedidos import menu_pedidos
from menus.menu_productos import menu_productos
from colorama import init, Fore, Style

init(autoreset=True)

def mostrar_menu(db):
    while True:
        ancho = 40
        print(Fore.CYAN + "=" * ancho)
        print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ PRINCIPAL")
        print(Fore.CYAN + "=" * ancho)
        print(Fore.GREEN + "1. Clientes")
        print(Fore.GREEN + "2. Pedidos")
        print(Fore.GREEN + "3. Productos")
        print(Fore.RED + "q. Salir")
        print(Fore.CYAN + "=" * ancho)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes(db)  
        elif opcion == "2":
            menu_pedidos(db)
        elif opcion == "3":
            menu_productos(db)
        elif opcion.lower() == "q":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
