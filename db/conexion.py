from pymongo import MongoClient
import getpass

def connect(db_name: str=""):
    user = input("Usuario MongoDB [admin]: ") or "admin"
    pwd = getpass.getpass("Contraseña MongoDB: ")
    host = input("Host MongoDB [localhost]: ") or "localhost"
    port_input = input("Puerto MongoDB [27017]: ")
    port = int(port_input) if port_input else 27017
    uri = f"mongodb://{user}:{pwd}@{host}:{port}/?authSource=admin"
    cliente = MongoClient(uri)
    return cliente[db_name]