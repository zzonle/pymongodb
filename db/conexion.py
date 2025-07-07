from colorama import init, Fore, Style
from pymongo import MongoClient
import getpass
init(autoreset=True)

def connect(db_name: str=""):
    while True:
        user = input(Fore.YELLOW + "Usuario MongoDB: " + Style.RESET_ALL)
        pwd = getpass.getpass(Fore.YELLOW + "Contraseña MongoDB: " + Style.RESET_ALL)
        if not user or not pwd:
            print(Fore.RED + "Usuario y/o contraseña no pueden estar vacíos." + Style.RESET_ALL)
            continue
        
        confirmar = input(Fore.CYAN + "¿Desea continuar con estos datos? (s/n): " + Style.RESET_ALL)
        if confirmar.lower() != 's':
            continue
        else:
            break
    host = "localhost"
    port = 27017
    uri = f"mongodb://{user}:{pwd}@{host}:{port}/?authSource=admin"
    cliente = MongoClient(uri)
    try:
            cliente.admin.command("ping")  
            return cliente[db_name]
    except Exception as e:
            print(Fore.RED + "Error de credenciales y/o conectar con ComercioTech", str(e) + Style.RESET_ALL)
            return None

"""
def connect(db_name="comerciotech"):
    user = input("Usuario MongoDB Atlas: ") or "comercioTech"
    pwd = getpass.getpass("Contraseña MongoDB Atlas: ") or 'KJntbc0OhgOSSi4c'
    uri = f"mongodb+srv://{user}:{pwd}@{db_name}.sygfbbv.mongodb.net/{db_name}?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client[db_name]
    return db
"""
