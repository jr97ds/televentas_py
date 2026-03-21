from personas import Cliente
from abc import ABC
from producto import Producto

class OrdenCompra:

    _contador = 0

    def __init__(self, cliente : Cliente):
        OrdenCompra._contador += 1
        self._id_orden = f"OC-{OrdenCompra._contador}"
        self._cliente = cliente
        self._detalles = []
        self._total = 0
        self._estado = "Abierta"
        self._metodo_pago = None

    @property
    def estado(self):
        return self._estado
    
    @property
    def detalles(self):
        return self._detalles
    
    @property
    def total(self):
        return self._total
    
    @property
    def id_orden(self):
        return self._id_orden

    # Metodo para agregar productos a la orden de compra
    def agregar_producto(self, producto : Producto, cantidad : int) -> None:
        detalle = DetalleOrden(producto, cantidad)
        self._detalles.append(detalle)
        self._total += detalle.subtotal

    # Metodo para eliminar productos de la orden de compra 
    def eliminar_producto(self, id_producto : str) -> None:
        for detalle in self._detalles:
            if detalle._producto.id_producto == id_producto:
                self._total -= detalle.subtotal
                self._detalles.remove(detalle)
                break

    # Metodo para agregar metodo de pago a la orden de compra
    def agregar_metodo_pago(self, metodo_pago : MetodoPago) -> None:
        self._metodo_pago = metodo_pago
        self._estado = "Pagada"
    

class DetalleOrden:

    def __init__(self, producto : Producto, cantidad : int):
        self._producto = producto
        self._cantidad = cantidad
        self._subtotal = producto.precio * cantidad

    @property
    def subtotal(self):
        return self._subtotal
    
    def calculo_subtotal(self) -> float:
        return self._producto.precio * self._cantidad
    
    def __str__(self) -> str:
        return f"{self._cantidad} x {self._producto.id_producto} {self._producto.nombre} - Subtotal: ${self._subtotal}"

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