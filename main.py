from colorama import init, Fore, Style
from menus.principal import mostrar_menu
from db.conexion import connect

init(autoreset=True)


if __name__ == "__main__":
    while True:
        try:
            db = connect("comerciotech")
            if db is not None:
                break
        except Exception as e:
            print(Fore.RED + "Error al conectar con MongoDB:", e + Style.RESET_ALL)
            retry = input(Fore.YELLOW + "¿Reintentar? (s/n): " + Style.RESET_ALL)
            if retry.lower() != "s":
                break
    
    mostrar_menu(db)