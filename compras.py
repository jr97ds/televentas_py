from personas import Cliente
from abc import ABC
from producto import Inventario, Producto

class MetodoPago(ABC):
    pass
    

class TarjetaCredito(MetodoPago):

    def __init__(self, numero : str, titular : str, 
                 fecha_expiracion : str, cvv : str):
        self._numero = numero
        self._titular = titular
        self._fecha_expiracion = fecha_expiracion
        self._cvv = cvv


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
        self._orden_envio = None

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
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def orden_envio(self):
        return self._orden_envio
    
    @orden_envio.setter
    def orden_envio(self, orden_envio): 
        self._orden_envio = orden_envio
    
    @estado.setter
    def estado(self, nuevo_estado : str):
        self._estado = nuevo_estado

    # Metodo para agregar productos a la orden de compra
    def agregar_producto(self, producto : Producto, cantidad : int) -> bool:
        if cantidad > producto.stock:
            print(f"\n" + f"No hay suficiente stock para el producto "
                  f"{producto.nombre}. Stock disponible: {producto.stock}")
            return False 
        else:
            detalle = DetalleOrden(producto, cantidad)
            self._detalles.append(detalle)
            self._total += detalle.subtotal
            return True 

    # Metodo para eliminar productos de la orden de compra 
    def eliminar_producto(self, id_producto : str) -> None:
        for detalle in self._detalles:
            if detalle.producto.id_producto == id_producto:
                self._total -= detalle.subtotal
                self._detalles.remove(detalle)
                break

    # Metodo para agregar metodo de pago a la orden de compra
    def agregar_metodo_pago(self, metodo_pago : MetodoPago) -> None:
        self._metodo_pago = metodo_pago
        self._estado = "Pagada"
    
    def actualizar_inventario(self,inventario : Inventario) -> None:
        for detalle in self._detalles:
            nuevo_stock = detalle.producto.stock - detalle.cantidad
            inventario.modificar_inventario_externo(detalle.producto, 
                                                    nuevo_stock) 
    
    def devolver_a_inventario(self, inventario : Inventario) -> None:
        for detalle in self._detalles:
            nuevo_stock = detalle.producto.stock + detalle.cantidad
            inventario.modificar_inventario_externo(detalle.producto, 
                                                    nuevo_stock) 

    def __str__(self) -> str:
        return (
            f"ID: {self._id_orden} - "
            f"Cliente: {self._cliente.nombre_completo} - "
            f"Total: ${self._total} - "
            f"Estado: {self._estado} - "
            f"Transportista: {self._orden_envio.transportista.nombre 
                              if self._orden_envio else 'No asignado'}"
        )


class DetalleOrden:

    def __init__(self, producto : Producto, cantidad : int):
        self._producto = producto
        self._cantidad = cantidad
        self._subtotal = producto.precio * cantidad
    
    @property
    def producto(self):
        return self._producto

    @property
    def subtotal(self):
        return self._subtotal
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def calculo_subtotal(self) -> float:
        return self._producto.precio * self._cantidad
    
    def __str__(self) -> str:
        return (f"{self._cantidad} x {self._producto.id_producto} "
                f"{self._producto.nombre} - Subtotal: ${self._subtotal}")

class Queja:

    _contador = 0

    def __init__(self, cliente : Cliente, descripcion : str, 
                 id_orden : str = None): # type: ignore
        Queja._contador += 1
        self._id_queja = f"PQR-{Queja._contador}"
        self._id_orden = id_orden
        self._cliente = cliente
        self._descripcion = descripcion
        self._estado = "Pendiente"
    
    def __str__(self) -> str:
        return(
            f"ID: {self._id_queja} -id_orden: {self._id_orden} - "
            f"Cliente: {self._cliente.nombre_completo} -Descripción: "
            f"{self._descripcion} - Estado: {self._estado}"
        )

