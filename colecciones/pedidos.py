"""pedidos
{
  "cliente_id": ObjectId(),
  "fecha": "2025-07-01T12:00:00Z",
  "productos": [
    { "producto_id": ObjectId(), "cantidad": 2 }
  ],
  "total": 499980,
  "estado": "Procesado"
} 
"""
from datetime import datetime
from colorama import init, Fore, Style
from bson.objectid import ObjectId
init(autoreset=True)

def leer_pedidos(db):
    try:
        pedidos = db.pedidos.find()
        if not pedidos:
            print(Fore.RED + "No hay pedidos.")
            return

        for pedido in pedidos:
            print(Fore.CYAN + "=" * 40)
            print(f"Cliente_id: {pedido['cliente_id']}")
            print(f"Fecha     : {pedido['fecha']}")
            print(f"Productos : {pedido['productos']}")
            print(f"Total     : {pedido['total']}")
            print(f"Estado    : {pedido['estado']}")
            print(Fore.CYAN + "=" * 40)
    except Exception as e:
        print(Fore.RED + "Error al buscar pedidos:", e, Style.RESET_ALL)

def leer_pedidos_por_id(db):
    try:
        id = input("Ingrese el id del pedido: ")
        pedido = db.pedidos.find_one({ "_id": ObjectId(id) })
        
        if not pedido:
            print(Fore.RED + "Pedido no encontrado." + Style.RESET_ALL)
            return

        print(Fore.CYAN + "=" * 40)
        print(f"Cliente_id: {pedido['cliente_id']}")
        print(f"Fecha     : {pedido['fecha']}")
        print(f"Total     : {pedido['total']}")
        print(f"Estado    : {pedido['estado']}")
        print("Productos:")
        for item in pedido['productos']:
            print(f"  - ID: {item['producto_id']} | Cantidad: {item['cantidad']}")

        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al buscar pedido:", e, Style.RESET_ALL)

def agregar_pedido(db):
    try:
        print("Clientes disponibles:")
        for c in db.clientes.find():
            print(f" - {c['nombre']} | ID: {c['_id']}")

        cliente_id = input("Ingrese el ID del cliente: ").strip()
        try:
            cliente_id = ObjectId(cliente_id)
        except:
            print(Fore.RED + "ID inválido." + Style.RESET_ALL)
            return

        if not db.clientes.find_one({ "_id": cliente_id }):
            print(Fore.RED + "Cliente no encontrado." + Style.RESET_ALL)
            return

        productos = []
        total = 0

        while True:
            print("Productos disponibles:")
            for p in db.productos.find():
                print(f" - {p['nombre']} | ID: {p['_id']} | Precio: {p['precio']} | Stock: {p['stock']}")
            producto_id = input("Ingrese el ID del producto (o enter para terminar): ").strip()
            if not producto_id:
                break

            try:
                producto_obj_id = ObjectId(producto_id)
            except:
                print(Fore.RED + "ID inválido." + Style.RESET_ALL)
                continue

            producto = db.productos.find_one({ "_id": producto_obj_id })
            if not producto:
                print(Fore.RED + "Producto no encontrado." + Style.RESET_ALL)
                continue

            cantidad = int(input(f"Ingrese la cantidad para '{producto['nombre']}' (stock disponible: {producto['stock']}): "))
            if cantidad <= 0:
                print(Fore.YELLOW + "Cantidad inválida." + Style.RESET_ALL)
                continue

            if cantidad > int(producto["stock"]):
                print(Fore.RED + "No hay suficiente stock." + Style.RESET_ALL)
                continue

            subtotal = int(producto["precio"]) * cantidad
            total += subtotal
            productos.append({
                "producto_id": producto["_id"],
                "cantidad": cantidad
            })

        if not productos:
            print(Fore.RED + "No se agregaron productos al pedido." + Style.RESET_ALL)
            return

        pedido = {
            "cliente_id": cliente_id,
            "fecha": datetime.now(),
            "productos": productos,
            "total": total,
            "estado": "Pendiente"
        }

        db.pedidos.insert_one(pedido)

        for item in productos:
            db.productos.update_one(
                { "_id": item["producto_id"] },
                { "$inc": { "stock": -item["cantidad"] } }
            )
        print(Fore.GREEN + "Pedido agregado exitosamente y stock actualizado." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + "Error al agregar pedido:", e, Style.RESET_ALL)


def actualizar_pedido(db):
    try:
        id = input("Ingrese el ID del pedido a actualizar: ")
        pedido = db.pedidos.find_one({ "_id": ObjectId(id) })
        if not pedido:
            print(Fore.RED + "Pedido no encontrado." + Style.RESET_ALL)
            return
        estado = input("Ingrese el nuevo estado del pedido (Pendiente, Procesado, Enviado, Entregado): ").strip()
        if estado not in ["Pendiente", "Procesado", "Enviado", "Entregado"]:
            print(Fore.RED + "Estado inválido." + Style.RESET_ALL)
            return
        db.pedidos.update_one({ "_id": ObjectId(id) }, { "$set": { "estado": estado } })
        print(Fore.GREEN + "Pedido actualizado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al actualizar pedido:", e, Style.RESET_ALL)

def eliminar_pedido(db):
    try:
        id = input("Ingrese el ID del pedido a eliminar: ")
        resultado = db.pedidos.delete_one({ "_id": ObjectId(id) })
        if resultado.deleted_count == 0:
            print(Fore.RED + "Pedido no encontrado." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Pedido eliminado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al eliminar pedido:", e, Style.RESET_ALL)
