from pymongo import MongoClient
import getpass

def connect(db_name: str=""):
    user = input("Usuario MongoDB: ")
    pwd = getpass.getpass("Contraseña MongoDB: ") 
    host = "localhost"
    port = 27017
    uri = f"mongodb://{user}:{pwd}@{host}:{port}/?authSource=admin"
    cliente = MongoClient(uri)
    return cliente[db_name]

"""
def connect(db_name="comerciotech"):
    user = input("Usuario MongoDB Atlas: ") or "comercioTech"
    pwd = getpass.getpass("Contraseña MongoDB Atlas: ") or 'KJntbc0OhgOSSi4c'
    uri = f"mongodb+srv://{user}:{pwd}@{db_name}.sygfbbv.mongodb.net/{db_name}?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client[db_name]
    return db
"""
