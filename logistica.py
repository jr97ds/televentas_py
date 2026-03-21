from compras import OrdenCompra
from personas import Cliente

class OrdenEnvio:
    def __init__(self,  orden_compra : OrdenCompra):
        self._orden_compra = orden_compra
        self._transportista = None
        self._estado_envio = "Enviada"

    @property
    def orden_compra(self):
        return self._orden_compra
    
    @property
    def transportista(self):
        return self._transportista
    
    @property
    def estado_envio(self):
        return self._estado_envio
    
    @estado_envio.setter
    def estado_envio(self, nuevo_estado : str):
        self._estado_envio = nuevo_estado

    @transportista.setter
    def transportista(self, empresa_transporte: EmpresaTransporte):
        self._transportista = empresa_transporte

class EmpresaTransporte:

    def __init__(self, nombre : str):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre