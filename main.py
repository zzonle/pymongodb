from menus.principal import mostrar_menu
from db.conexion import connect

if __name__ == "__main__":
    while True:
        try:
            db = connect("comerciotech")
            if db is not None:
                break
        except Exception as e:
            print("Error al conectar con MongoDB:", e)
            retry = input("¿Reintentar? (s/n): ")
            if retry.lower() != "s":
                break
    
    mostrar_menu(db)