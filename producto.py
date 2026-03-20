from personas import Cliente
from abc import ABC
class Producto: 

    def __init__(self, id_producto : str, nombre : str, 
        descripcion : str, precio : float, stock : int):

        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock


class Catalogo:
    def __init__(self):
        self.productos = []


class Suscripcion:

    def __init__(self, cliente : Cliente, peridiocidad : str):
        self.cliente = cliente
        self.peridiocidad = peridiocidad
        self.status = "Activa"


class Inventario(ABC):

