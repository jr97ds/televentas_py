from compras import OrdenCompra
from personas import Cliente
from producto import Producto , InventarioExcel , Catalogo , Suscripcion

jose = Cliente("Jose", "Rojas", "Calle 123", "jose@gmail.com")

clientes = [jose]
cliente_actual = None
login = False

#Creación de Productos a partir del inventario externo
inventario = InventarioExcel("inventario_televentas.xlsx")

# Funcion para inicializar el catalogo a partir de productos creados con inventairo
def inicializar_catalogo(inventario : InventarioExcel) -> Catalogo:
    catalogo = Catalogo()
    for item in inventario.cargar_inventario_externo():
        catalogo.agregar_producto(item)

    return catalogo


# menu para seleccionar portal de clientes o empleados
def menu_usuario():
    print("\n" + "----- TeleVentas -----")
    print("1. Portal Clientes")
    print("2. Portal Empleados")


# Funcion para crear nuevos clientes y añadirlos a la lista de clientes registrados
def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    direccion = input("Ingrese su dirección: ")
    correo = input("Ingrese su correo electrónico: ")
    print("\n" + f"{nombre} , has sido registrado exitosamente")
    return Cliente(nombre, apellido, direccion, correo)

def mostrar_orden_actual(orden_compra_actual : OrdenCompra):
    print("\n" + "Orden Actual:")
    for item in orden_compra_actual.detalles: 
        print(item)

# --------------------Inicialización del programa-------------------- #

catalogo = inicializar_catalogo(inventario)

while True:
    menu_usuario()
    opcion_portal = input("\n" + "Seleccione una opción: ")

    # Portal Clientes
    if opcion_portal == "1":
        print("\n" + "Bienvenido al Portal de Clientes")

        print("\n" + "Seleccione una de las siguientes opciones")
        print("1. Soy cliente nuevo")
        print("2. Soy cliente registrado")
        print("3. Volver al menú principal")

        opcion_cliente = input("\n" + "Seleccione una opción: ")

        # Registro Usuario Nuevo
        if opcion_cliente == "1":
            print("\n" + "Por favor regístrese para continuar")
            cliente_actual = crear_cliente()
            # añadir cliente a la lista de clientes registrados
            clientes.append(cliente_actual)
            login = True

        # Login Usuario Registrado
        elif opcion_cliente == "2":
            print("\n" + "Por favor inicie sesión para continuar")
            while not login: 
                correo = input("Ingrese su correo electrónico: ")
                encontrado = False
                for c in clientes:
                    if c.correo == correo:
                        cliente_actual = c
                        login = True
                        encontrado = True
                        break
                if not encontrado:
                        print("\n" + "Correo no encontrado, por favor intente de nuevo")

        # Volver al menú principal
        elif opcion_cliente == "3":
            continue


        # Desde aqui sigue la logica de un cliente loggeado
        print("\n" + f"Bienvenido, {cliente_actual.nombre} {cliente_actual.apellido}!")     # type: ignore

        #menu para cliente loggeado
        while login:    
            print("\n" + "Seleccione una de las siguientes opciones")   
            print("1. Ver catálogo de productos")
            print("2. Ver mis órdenes de compra")
            print("3. Ver mis quejas")
            print("4. Suscribirme al catálogo")
            print("0. Cerrar sesión")

            opcion_cliente_loggeado = input("\n" + "¿Que desea hacer?: ")


            # Mostrar Catalogo de Productos
            if opcion_cliente_loggeado == "1":
                print("\n" + "Catálogo de Productos:")
                catalogo.mostrar_catalogo()

                while True:
                    # Menu en vista de catalogo
                    print("\n" + "¿Que desea hacer?")
                    print("1. Realizar una orden de compra")
                    print("2. Volver al menú anterior")
                    opcion_orden = input("\n" + "Seleccione una opción: ")

                 # Crear Orden de Compra desde el cliente loggeado
                    if opcion_orden == "1":
                        orden_compra_actual = cliente_actual.crear_orden_compra() # type: ignore

                        while orden_compra_actual.estado == "Abierta":
                            id_producto_a_añadir = input("\n" + "Ingrese el ID del producto que desea agregar a su orden: ").upper()
                            cantidad_a_añadir = int(input("Ingrese la cantidad que desea agregar: "))
                        
                            producto_a_añadir = None

                            for producto in catalogo._productos:
                                if producto.id_producto == id_producto_a_añadir:
                                    producto_a_añadir = producto
                                    break
                        
                            if producto_a_añadir is None:
                                print("\n" + "Producto no encontrado, por favor intente de nuevo")
                                continue

                            if cantidad_a_añadir <= 0:
                                print("\n" + "Cantidad inválida, por favor ingrese una cantidad mayor a 0")
                                continue


                            orden_compra_actual.agregar_producto(producto_a_añadir, cantidad_a_añadir) # type: ignore

                            print("\n" + f"{cantidad_a_añadir} unidades de {producto_a_añadir.nombre} agregadas")

                            mostrar_orden_actual(orden_compra_actual)

                            while True:
                                status_orden = input("\n" + "Escriba '1' para continuar agregando productos, '2' para eliminar un producto, o '0' para finalizar su orden: ")
                                
                                if status_orden == "1":
                                    break

                                # Terminar proceso de compra y pasar a pago
                                if status_orden == "0":
                                    orden_compra_actual._estado = "Pendiente Pago" 
                                    print("\n" + "Orden lista para pago, por favor agregue su metodo de pago")
                                    break
                            
                                # Eliminar producto de la orden de compra
                                elif status_orden == "2":
                                    id_producto_a_eliminar = input("\n" + "Ingrese el ID del producto que desea eliminar de su orden: ").upper()
                                    
                                    for detalle in orden_compra_actual.detalles: 
                                        if detalle._producto.id_producto == id_producto_a_eliminar:
                                            orden_compra_actual.eliminar_producto(id_producto_a_eliminar) 
                                            print("\n" + f"Producto  eliminado de su orden")
                                            mostrar_orden_actual(orden_compra_actual)
                                            continue

                                        else :
                                            print("\n" + "Producto no encontrado en su orden, por favor intente de nuevo")
                                            break
                                    
                    # Desde catalogo , regresar a menu cliente loggeado
                    elif opcion_orden == "2":
                        break

                    else:
                        print("\n" + "Opción inválida, por favor seleccione una opción válida")
                        continue

                                                
            # SEGUIR AQUI Procedimiento para agregar metodo de pago a la orden de compra -SEGUIR AQUI
                print("\n" + "Seleccione su método de pago")

            # Cierre Sesion Cliente
            elif opcion_cliente_loggeado == "0":
                    print("\n" + "Cerrando sesión...")
                    login = False
                    cliente_actual = None
                
            

        











    # Portal Empleados 
    elif opcion_portal == "2":
        print("\n" + "Bienvenido al Portal de Empleados")
        # lógica de crear orden
    else:
        print("\n" + "Opción Invalida, por favor seleccione una opción válida")



menu_usuario()