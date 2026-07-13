
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre: str) -> Producto | None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.strip().lower():
                return producto
        return None

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, id_cliente: str) -> Cliente | None:
        for cliente in self.clientes:
            if cliente.id_cliente.strip() == id_cliente.strip():
                return cliente
        return None
