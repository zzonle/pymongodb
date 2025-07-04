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
        cliente_id = input("Ingrese el ID del cliente: ")
        if not db.clientes.find_one({ "_id": ObjectId(cliente_id) }):
            print(Fore.RED + "Cliente no encontrado." + Style.RESET_ALL)
            return
        productos = []
        total = 0
        while True:
            producto_id = input("Ingrese el ID del producto (o enter para terminar): ").strip()
            if not producto_id:
                break
            try:
                producto = db.productos.find_one({ "_id": ObjectId(producto_id) })
                if not producto:
                    print(Fore.RED + "Producto no encontrado." + Style.RESET_ALL)
                    continue
                cantidad = int(input(f"Ingrese la cantidad para '{producto['nombre']}': "))
                subtotal = producto["precio"] * cantidad
                total += subtotal
                productos.append({
                    "producto_id": producto["_id"],
                    "cantidad": cantidad
                })
            except Exception as e:
                print(Fore.RED + "Error con el producto:", e, Style.RESET_ALL)
                continue
        if not productos:
            print(Fore.RED + "No se agregaron productos al pedido." + Style.RESET_ALL)
            return
        pedido = {
            "cliente_id": ObjectId(cliente_id),
            "fecha": datetime.utcnow().isoformat(),
            "productos": productos,
            "total": total,
            "estado": "Pendiente"
        }
        db.pedidos.insert_one(pedido)
        print(Fore.GREEN + "Pedido agregado exitosamente." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error al agregar pedido:", e, Style.RESET_ALL)
   