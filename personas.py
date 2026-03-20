from abc import ABC, abstractmethod


# Clase abstracta que sirve de base para todas los usuarios involucrados
class Persona(ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str):
        
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        
        
# Clase para clientes
class Cliente(Persona):

    def __init__(self, nombre : str, apellido : str, 
                 direccion : str, correo : str):
        super().__init__(nombre, apellido, correo)
        self._direccion = direccion
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
    def direccion(self):
        return self._direccion
    
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

# Clase abstracta para empleados
class Empleado(Persona, ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo)
        self._usuario = usuario
        self._contraseña = contraseña

class AgenteDeposito(Empleado):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo, usuario, 
                         contraseña)
        
class GerenteRP(Empleado):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo, usuario, 
                         contraseña)