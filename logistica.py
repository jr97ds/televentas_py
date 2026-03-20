from compras import OrdenCompra
from personas import Cliente

class OrdenEnvio:
    def __init__(self, cliente : Cliente, 
                 orden_compra : OrdenCompra):
        self.cliente = cliente
        self.orden_compra = orden_compra
        self.transportista = None
        self.estado_envio = "Pendiente"

class EmpresaTransporte:

    def __init__(self, nombre : str):
        self.nombre = nombre