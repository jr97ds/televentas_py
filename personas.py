from abc import ABC, abstractmethod

from compras import OrdenCompra
from logistica import EmpresaTransporte

# Clase abstracta que sirve de base para todas los usuarios involucrados
class Persona(ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str):
        
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
    
    @abstractmethod
    def nombre_completo(self):
        pass
        
# Clase para clientes
class Cliente(Persona):

    def __init__(self, nombre : str, apellido : str, correo : str):
        super().__init__(nombre, apellido, correo)
        self._suscripcion = None
        self._quejas = []
        self._ordenes_compra = []

    @property
    def correo(self):
        return self._correo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"
    
    @property
    def ordenes_compra(self):
        return self._ordenes_compra
    
    @property
    def suscripcion(self):
        return self._suscripcion
    
    @property
    def quejas(self):
        return self._quejas
    
    @suscripcion.setter
    def suscripcion(self, tipo_suscripcion : str):
        self._suscripcion = tipo_suscripcion
    

# Clase abstracta para empleados
class Empleado(Persona, ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo)
        self._usuario = usuario
        self._contraseña = contraseña
        self._cargo = None

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"
    
    @property
    def usuario(self):
        return self._usuario
    
    @property
    def cargo(self):
        return self._cargo
    
    @property
    def contraseña(self):
        return self._contraseña
    
class AgenteDeposito(Empleado):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo, usuario, 
                         contraseña)
        self._cargo = "Agente"

    @property
    def contraseña(self): 
        return self._contraseña
    
    def alistar_orden_para_envio(self, 
                                 orden_compra : OrdenCompra, 
                                 transportista : EmpresaTransporte) -> None:
        from logistica import OrdenEnvio
        
        if orden_compra.estado == "Pagada":
            envio = OrdenEnvio(orden_compra)
            envio.transportista = transportista 
            orden_compra.estado = "Enviada"
            orden_compra.orden_envio = envio 

            print(f"\n" + f"Orden {orden_compra.id_orden} "
                  f"alistada para envío.")
        else:
            print(f"\n" + f"Orden {orden_compra.id_orden} "
                  f"no se encuentra en estado pagada.")

class GerenteRP(Empleado):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo, usuario, 
                         contraseña)
        self._cargo = "Gerente"
    
    
    # Metodo para mostrar quejas registradas en el sistema
    def mostrar_quejas(self, quejas : list) -> None:
        if not quejas:
            print("\n" + "No hay quejas registradas en el sistema.")
        else:
            print("\n" + "Quejas Registradas:")
            for queja in quejas:
                print(f"- {queja}")