from pymongo import MongoClient
import getpass

def connect(db_name: str=""):
    user = input("Usuario MongoDB [admin]: ") or "usuario"
    pwd = getpass.getpass("Contraseña MongoDB: ") or 'comercioTech123'
    host = input("Host MongoDB [localhost]: ") or "localhost"
    port_input = input("Puerto MongoDB [27017]: ")
    port = int(port_input) if port_input else 27017
    uri = f"mongodb://{user}:{pwd}@{host}:{port}/?authSource={db_name or 'admin'}"
    cliente = MongoClient(uri)
    return cliente[db_name]