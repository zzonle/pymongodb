from colorama import init, Fore, Style
from bson.objectid import ObjectId

init(autoreset=True)

def leer_clientes(db):
    try:
        clientes = db.clientes.find()
        for cliente in clientes:
            print(Fore.CYAN + "=" * 40)
            print(f"Nombre    : {cliente['nombre']}")
            print(f"Email     : {cliente['email']}")
            print(f"Teléfono  : {cliente['telefono']}")
            print(f"Dirección : {cliente['direccion']}")
            print(f"Id        : {cliente['_id']}")
            print(Fore.CYAN + "=" * 40)
    except Exception as e:
        print(Fore.RED + "Error al buscar clientes:", e, Style.RESET_ALL)

def leer_clientes_por_id(db):
    try:
        id = input("Ingrese el id del cliente: ")
        cliente = db.clientes.find_one({ "_id": ObjectId(id) })
        if not cliente:
            print(Fore.RED + "Cliente no encontrado." + Style.RESET_ALL)
            return
        
        print(Fore.CYAN + "=" * 40)
        print(f"Nombre    : {cliente['nombre']}")
        print(f"Email     : {cliente['email']}")
        print(f"Teléfono  : {cliente['telefono']}")
        print(f"Dirección : {cliente['direccion']}")
        print(f"Id        : {cliente['_id']}")
        print(Fore.CYAN + "=" * 40) 
    except Exception as e:
        print(Fore.RED + "Error al buscar cliente:", e, Style.RESET_ALL)

def agregar_cliente(db):
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        cliente = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "direccion": direccion
        }
        db.clientes.insert_one(cliente)
        print(Fore.GREEN + "Cliente agregado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al agregar cliente:", e, Style.RESET_ALL)

def agregar_varios_clientes(db):
    try:
        clientes = []
        while True:
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            direccion = input("Ingrese la direccion del cliente: ")
            clientes.append({
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "direccion": direccion
            })
            opcion = input("Desea agregar otro cliente? (s/n): ")
            if opcion.lower() != "s":
                break
        db.clientes.insert_many(clientes)
        print(Fore.GREEN + "Clientes agregados exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al agregar clientes:", e, Style.RESET_ALL)

def actualizar_cliente(db):
    try:
        id = input("Ingrese el id del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        cliente = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "direccion": direccion
        }
        db.clientes.update_one({"_id": ObjectId(id)}, {"$set": cliente})
        print(Fore.GREEN + "Cliente actualizado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al actualizar cliente:", e, Style.RESET_ALL)

def eliminar_cliente(db):
    try:
        id = input("Ingrese el id del cliente: ")
        db.clientes.delete_one({"_id": ObjectId(id)})
        print(Fore.GREEN + "Cliente eliminado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al eliminar cliente:", e, Style.RESET_ALL)
