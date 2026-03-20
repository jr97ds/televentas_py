from personas import Cliente
from abc import ABC
from producto import Producto

class OrdenCompra:

    _contador = 0

    def __init__(self, cliente : Cliente, metodo_pago : MetodoPago):
        OrdenCompra._contador += 1
        self._id_orden = f"OC-{OrdenCompra._contador}"
        self._cliente = cliente
        self._detalles = []
        self._total = 0
        self._estado = "En proceso"
        self._metodo_pago = metodo_pago

class DetalleOrden:

    def __init__(self, producto : Producto, cantidad : int):
        self._producto = producto
        self._cantidad = cantidad
        self._subtotal = producto.precio * cantidad

class Queja:

    _contador = 0

    def __init__(self, cliente : Cliente, descripcion : str):
        Queja._contador += 1
        self._id_queja = f"PQR-{Queja._contador}"
        self._cliente = cliente
        self._descripcion = descripcion
        self._estado = "Pendiente"

class MetodoPago(ABC):
    pass
    
class TarjetaCredito(MetodoPago):

    def __init__(self, numero : str, titular : str, 
                 fecha_expiracion : str, cvv : str):
        self._numero = numero
        self._titular = titular
        self._fecha_expiracion = fecha_expiracion
        self._cvv = cvv