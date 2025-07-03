       
from colorama import init, Fore, Style
init(autoreset=True)

def menu_clientes():
    while True:
        ancho = 40
        print(Fore.CYAN + "=" * ancho)
        print(Fore.CYAN + " " * ((ancho - 12)//2) + Style.BRIGHT + "MENÚ CLIENTES")
        print(Fore.CYAN + "=" * ancho)
        print(Fore.GREEN + "1. Mostrar cliente")
        print(Fore.GREEN + "2. Agregar cliente")
        print(Fore.GREEN + "3. Actualizar cliente")
        print(Fore.GREEN + "4. Eliminar cliente")
        print(Fore.RED + "q. Volver menú principal")
        print(Fore.CYAN + "=" * ancho)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for i in range(100):
                print(f"numeros randos{i}")
            input("Presione ENTER para volver al menú de clientes...")
        elif opcion.lower() == "q":
            break
        else:
            print("Opción no válida. Intente de nuevo.")




    

    