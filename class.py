
# Clase del Cliente que accede al sistema para hacer compra/revisar pedidos

class Cliente:
    def __init__(self, nombre : str, apellido : str, 
                 direccion : str, correo : str, telefono : str):
        
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono
        self.suscripcion = None
        self.quejas = []
        self.ordenes_compra = []




