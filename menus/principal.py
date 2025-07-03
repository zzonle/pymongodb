from menus.menu_clientes import menu_clientes 
from colorama import init, Fore, Style

init(autoreset=True)

def mostrar_menu():
    ancho = 40
    print(Fore.CYAN + "=" * ancho)
    print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ PRINCIPAL")
    print(Fore.CYAN + "=" * ancho)
    print(Fore.GREEN + "1. Clientes")
    print(Fore.GREEN + "2. Pedidos")
    print(Fore.GREEN + "3. Productos")
    print(Fore.RED + "q. Salir")
    print(Fore.CYAN + "=" * ancho)

