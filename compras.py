from personas import Cliente

class OrdenCompra:

    _contador = 0

    def __init__(self, cliente : Cliente, metodo_pago : MetodoPago):
        OrdenCompra._contador += 1
        self.id_orden = f"OC-{OrdenCompra._contador}"
        self.cliente = cliente
        self.detalles = []
        self.total = 0
        self.estado = "En proceso"
        self.metodo_pago = metodo_pago

class DetalleOrden:

    def __init__(self, producto : Producto, cantidad : int):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

class Queja:

    _contador = 0

    def __init__(self, cliente : Cliente, descripcion : str):
        Queja._contador += 1
        self.id_queja = f"PQR-{Queja._contador}"
        self.cliente = cliente
        self.descripcion = descripcion
        self.estado = "Pendiente"