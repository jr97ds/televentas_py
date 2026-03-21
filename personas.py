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
    
    @property
    def ordenes_compra(self):
        return self._ordenes_compra
    
    @property
    def suscripcion(self):
        return self._suscripcion
    
    @property
    def quejas(self):
        return self._quejas
    
    # Metodo para crear orden de compra desde el cliente loggeado
    def crear_orden_compra(self) -> OrdenCompra: # type: ignore
        from compras import OrdenCompra
        orden = OrdenCompra(self)
        self._ordenes_compra.append(orden)
        return orden
    
    def mostrar_ordenes_compra(self) -> None:
        if not self._ordenes_compra:
            print("\n" + "No tiene órdenes de compra registradas.")
        else:
            print("\n" + "Órdenes de Compra:")
            for orden in self._ordenes_compra:
                print(f"ID: {orden.id_orden} - Total: ${orden.total} - Estado: {orden.estado}")

    def borrar_orden_compra(self, id_orden : str) -> None:
        for orden in self._ordenes_compra:
            if orden.estado != "Enviado":
                if orden.id_orden == id_orden:
                    self._ordenes_compra.remove(orden)
                    print(f"\n" + f"Orden {id_orden} eliminada con éxito.")
                    break
        else:
            print(f"\n" + f"No se encontró una orden con ID {id_orden}.")
    
    def activar_suscripcion(self) -> None:
        from producto import Suscripcion
        if self._suscripcion is None:
            self._suscripcion = Suscripcion()
            print("\n" + "Suscripción activada con éxito.")
        elif self._suscripcion.status == "Cancelada":
            self._suscripcion._status = "Activa"
            print("\n" + "Suscripción reactivada con éxito.")
        else:
            print("\n" + "Ya tiene una suscripción activa.")
        
    
    def cancelar_suscripcion(self) -> None:
        if self._suscripcion is not None:
            self._suscripcion._status = "Cancelada"
            print("\n" + "Suscripción cancelada con éxito.")
        else:
            print("\n" + "No tiene una suscripción activa para cancelar.")

    def mostrar_quejas(self) -> None:
        if not self._quejas:
            print("\n" + "No tiene quejas registradas.")
        else:
            print("\n" + "Quejas Registradas:")
            for queja in self._quejas:
                print(f"- {queja}")

    def crear_queja(self, descripcion : str, id_orden : str = None) -> None: # type: ignore
        from compras import Queja
        queja = Queja(self, descripcion, id_orden=id_orden) # type: ignore
        self._quejas.append(queja)
        print("\n" + "Queja registrada con éxito.")


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