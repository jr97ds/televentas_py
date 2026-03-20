from compras import OrdenCompra
from personas import Cliente

class OrdenEnvio:
    def __init__(self, cliente : Cliente, 
                 orden_compra : OrdenCompra):
        self._cliente = cliente
        self._orden_compra = orden_compra
        self._transportista = None
        self._estado_envio = "Pendiente"

class EmpresaTransporte:

    def __init__(self, nombre : str):
        self._nombre = nombre