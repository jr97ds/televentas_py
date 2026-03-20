from abc import ABC, abstractmethod


# Clase abstracta que sirve de base para todas los usuarios involucrados
class Persona(ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str):
        
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        
        

class Cliente(Persona):

    def __init__(self, nombre : str, apellido : str, 
                 direccion : str, correo : str):
        super().__init__(nombre, apellido, correo)
        self.direccion = direccion
        self.suscripcion = None
        self.quejas = []
        self.ordenes_compra = []

class Empleado(Persona, ABC):

    def __init__(self, nombre : str, apellido : str, 
                 correo : str, usuario : str, contraseña : str):
        super().__init__(nombre, apellido, correo)
        self.usuario = usuario
        self.contraseña = contraseña

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