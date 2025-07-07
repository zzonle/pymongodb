from colorama import init, Fore, Style
from bson.objectid import ObjectId
init(autoreset=True)

def leer_productos(db):
    try:    
        productos = db.productos.find()
        for producto in productos:
            print(Fore.CYAN + "=" * 40)
            print(f"Nombre      : {producto['nombre']}")
            print(f"Categoria   : {producto['categoria']}")
            print(f"Precio      : {producto['precio']}")
            print(f"Stock       : {producto['stock']}")
            print(f"Id          : {producto['_id']}")
            print(Fore.CYAN + "=" * 40)
    except Exception as e:
        print(Fore.RED + "Error al buscar productos:", e + Style.RESET_ALL)

def leer_productos_por_id(db):
    try:
        id = input("Ingrese el id del producto: ")
        producto = db.productos.find_one({"_id": ObjectId(id)})
        print(Fore.CYAN + "=" * 40)
        print(f"Nombre      : {producto['nombre']}")
        print(f"Categoria   : {producto['categoria']}")
        print(f"Precio      : {producto['precio']}")
        print(f"Stock       : {producto['stock']}")
        print(f"Id          : {producto['_id']}")
        print(Fore.CYAN + "=" * 40) 
    except Exception as e:
        print(Fore.RED + "Error al buscar producto:", e + Style.RESET_ALL)

def agregar_producto(db):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoria del producto: ")
        precio = input("Ingrese el precio del producto: ")
        stock = input("Ingrese el stock del producto: ")
        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "stock": int(stock)
        }
        db.productos.insert_one(producto)
        print(Fore.GREEN + "Producto agregado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al agregar producto:", e + Style.RESET_ALL) 

def agregar_varios_productos(db):
    try:
        productos = []
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            precio = input("Ingrese el precio del producto: ")
            stock = input("Ingrese el stock del producto: ")
            productos.append({
                "nombre": nombre,
                "categoria": categoria,
                "precio": float(precio),
                "stock": int(stock)
            })
            opcion = input("Desea agregar otro producto? (s/n): ")
            if opcion.lower() != "s":
                break
        db.productos.insert_many(productos)
        print(Fore.GREEN + "Productos agregados exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al agregar productos:", e + Style.RESET_ALL)

def actualizar_producto(db):
    try:
        id = input("Ingrese el id del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoria del producto: ")
        precio = input("Ingrese el precio del producto: ")
        stock = input("Ingrese el stock del producto: ")
        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "stock": int(stock)
        }
        db.productos.update_one({"_id": ObjectId(id)}, {"$set": producto})
        print(Fore.GREEN + "Producto actualizado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED +"Error al actualizar producto:", e + Style.RESET_ALL)
    
def eliminar_producto(db):
    try:
        id = input("Ingrese el id del producto: ")
        db.productos.delete_one({"_id": ObjectId(id)})
        print(Fore.GREEN + "Producto eliminado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al eliminar producto:", e + Style.RESET_ALL)

