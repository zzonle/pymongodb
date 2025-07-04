from colorama import init, Fore
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
        print("Error al buscar productos:", e)

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
        print("Error al buscar producto:", e)

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
        print("Producto agregado exitosamente.")
    except Exception as e:
        print("Error al agregar producto:", e)

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
        print("Productos agregados exitosamente.")
    except Exception as e:
        print("Error al agregar productos:", e)

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
        print("Producto actualizado exitosamente.")
    except Exception as e:
        print("Error al actualizar producto:", e)
    
def eliminar_producto(db):
    try:
        id = input("Ingrese el id del producto: ")
        db.productos.delete_one({"_id": ObjectId(id)})
        print("Producto eliminado exitosamente.")
    except Exception as e:
        print("Error al eliminar producto:", e)

