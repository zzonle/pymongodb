from menus.principal import mostrar_menu
from menus.menu_clientes import menu_clientes

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()  # Entra al submenú y espera que termine
        elif opcion == "2":
            print("Menú pedidos aún no implementado.")
        elif opcion == "3":
            print("Menú productos aún no implementado.")
        elif opcion.lower() == "q":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
