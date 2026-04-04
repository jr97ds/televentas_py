from compras import OrdenCompra
from personas import Cliente
from producto import Suscripcion
from compras import Queja

class ServicioCliente: 
    """Clase que maneja los servicios relacionados con los clientes, 
    como la gestión de órdenes de compra, suscripciones y quejas."""
    
    # Metodo para crear orden de compra desde el cliente loggeado
    def crear_orden_compra(self, cliente: Cliente) -> OrdenCompra: 
        orden = OrdenCompra(cliente)
        cliente.ordenes_compra.append(orden)
        return orden
    
    def mostrar_ordenes_compra(self, cliente: Cliente) -> None:
        if not cliente.ordenes_compra:
            print("\n" + "No tiene órdenes de compra registradas.")
        else:
            print("\n" + "Órdenes de Compra:")
            for orden in cliente.ordenes_compra:
                print(orden)

    def borrar_orden_compra(self, id_orden : str, cliente: Cliente) -> None:
        for orden in cliente.ordenes_compra:
                if orden.id_orden == id_orden:
                    cliente.ordenes_compra.remove(orden)
                    print(f"\n" + f"Orden {id_orden} eliminada con éxito.")
                    break
        else:
            print(f"\n" + f"No se encontró una orden con ID {id_orden}.")
        
    def activar_suscripcion(self, cliente: Cliente) -> None:
        
        if cliente.suscripcion is None:
            cliente.suscripcion = Suscripcion()
            print("\n" + "Suscripción activada con éxito.")
        elif cliente.suscripcion.status == "Cancelada":
            cliente.suscripcion.reactivar()
            print("\n" + "Suscripción reactivada con éxito.")
        else:
            print("\n" + "Ya tiene una suscripción activa.")
        
    def cancelar_suscripcion(self, cliente: Cliente) -> None:
        if cliente.suscripcion is not None:
            cliente.suscripcion.cancelar()
            print("\n" + "Suscripción cancelada con éxito.")
        else:
            print("\n" + "No tiene una suscripción activa para cancelar.")

    def mostrar_quejas(self, cliente: Cliente) -> None:
        if not cliente.quejas:
            print("\n" + "No tiene quejas registradas.")
        else:
            print("\n" + "Quejas Registradas:")
            for queja in cliente.quejas:
                print(f"- {queja}")

    def crear_queja(self,cliente: Cliente, descripcion : str, 
                    id_orden : str) -> Queja:
        queja = Queja(cliente, descripcion, id_orden=id_orden) 
        cliente.quejas.append(queja)
        print("\n" + "Queja registrada con éxito.")
        return queja 