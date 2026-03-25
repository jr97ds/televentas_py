from compras import OrdenCompra, Queja, TarjetaCredito
from personas import Cliente, GerenteRP , AgenteDeposito
from producto import Inventario, InventarioExcel , Catalogo 
from logistica import EmpresaTransporte


# ----- CARGA DE DATOS PARA PRUEBAS ----- #
jose = Cliente("Jose", "Rojas", "jose@gmail.com")
clientes = [jose] # Lista para almacenar todos los clientes registrados
gerente = GerenteRP("Luis", "Perez", 
                    "gerente@televentas.com", "gerente", "1234")
agente = AgenteDeposito("Ana", "Gomez", "agente@televentas.com",
                        "agente", "1234")
empleados = [gerente, agente] # Lista empleados registrados en el sistema
empresa_t1 = EmpresaTransporte("Servientrega")
empresa_t2 = EmpresaTransporte("Coordinadora")
empresa_t3 = EmpresaTransporte("DHL")
transportistas = [empresa_t1, empresa_t2, empresa_t3] # Lista Transportistas
ordenes_compra = [] # Lista para almacenar todas las ordenes de compra 
quejas = [] # Lista para almacenar todas las quejas registradas 

# Variables de login
cliente_actual = None 
login = False

#Creación de Productos a partir del inventario externo
inventario = InventarioExcel("inventario_televentas.xlsx")

# Funcion para inicializar el catalogo a partir de 
# productos creados con inventairo
def inicializar_catalogo(inventario : InventarioExcel) -> Catalogo:
    catalogo = Catalogo()
    for item in inventario.cargar_inventario_externo():
        catalogo.agregar_producto(item)

    return catalogo

# menu para seleccionar portal de clientes o empleados
def menu_usuario() -> None:
    print("\n" + "----- TeleVentas -----")
    print("1. Portal Clientes")
    print("2. Portal Empleados")

# Funcion para crear nuevos clientes y añadirlos 
# a la lista de clientes registrados
def crear_cliente() -> Cliente:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    print("\n" + f"{nombre} , has sido registrado exitosamente")
    return Cliente(nombre, apellido, correo)

# Funcion para mostrar la orden de compra actual del cliente loggeado
def mostrar_orden_actual(orden_compra_actual : OrdenCompra) -> None:
    print("\n" + "Orden Actual:")
    for item in orden_compra_actual.detalles: 
        print(item)

# Funcion para mostrar mensaje de opcion invalida
def opcion_invalida() -> None:
    print("\n" + "Opción inválida, por favor seleccione una opción válida")

def proceso_orden(orden_compra_actual : OrdenCompra,
                 id_producto_a_eliminar : str) -> None:
    for detalle in orden_compra_actual.detalles: 
        if detalle.producto.id_producto == id_producto_a_eliminar:
            orden_compra_actual.eliminar_producto(id_producto_a_eliminar) 
            print("\n" + f"Producto  eliminado de su orden")
            mostrar_orden_actual(orden_compra_actual)
            break
        else:
            print("\n" + "Producto no encontrado "
                f"en su orden, por favor intente "
                f"de nuevo")
            break

# Funcion para mostrar el menu del cliente loggeado y gestionar sus opciones
def menu_cliente_loggeado(cliente_actual : Cliente,
                          catalogo : Catalogo,
                          inventario : InventarioExcel,
                          ordenes_compra : list[OrdenCompra],
                          quejas : list[Queja],
                          transportistas : list[EmpresaTransporte],
                          ) -> None:
    while True:    
        print("\n" + "----- MENU CLIENTE -----") 
        print("Seleccione una de las siguientes opciones")   
        print("1. Ver catálogo de productos")
        print("2. Ver mis órdenes de compra")
        print("3. Ver mis quejas")
        print("4. Suscribirme al catálogo")
        print("0. Cerrar sesión")

        opcion_cliente_loggeado = input("\n" + "¿Que desea hacer?: ")

        # Mostrar Catalogo de Productos
        if opcion_cliente_loggeado == "1":
            catalogo = inicializar_catalogo(inventario)
            print("\n" + "----- CATALOGO -----")
            catalogo.mostrar_catalogo()

            while True:
                # Menu en vista de catalogo
                print("\n" + "¿Que desea hacer?")
                print("1. Realizar una orden de compra")
                print("2. Volver al menú anterior")
                opcion_orden = input("\n" + "Seleccione una opción: ")

                # Crear Orden de Compra desde el cliente loggeado
                if opcion_orden == "1":
                    orden_compra_actual = cliente_actual.crear_orden_compra() 

                    while orden_compra_actual.estado == "Abierta":
                        id_producto_a_añadir = input(
                            "\n" + "Ingrese el ID del producto que "
                            f"desea agregar a su orden: "
                            ).upper()
                        cantidad_a_añadir = int(input(
                            "Ingrese la cantidad que desea agregar: "
                            ))
                        producto_a_añadir = None
                        producto_a_añadir = catalogo.buscar_producto(
                            id_producto_a_añadir
                            )

                        if producto_a_añadir is None:
                            print("\n" + "Producto no encontrado, "
                            f"por favor intente de nuevo")
                            continue

                        if cantidad_a_añadir <= 0:
                            print("\n" + "Cantidad inválida, "
                            f"por favor ingrese una cantidad mayor a 0")
                            continue

                        status= orden_compra_actual.agregar_producto(
                            producto_a_añadir, cantidad_a_añadir) # type: ignore

                        if status:
                            print("\n" + 
                                f"{cantidad_a_añadir} unidades de "
                                f"{producto_a_añadir.nombre} agregadas")

                        mostrar_orden_actual(orden_compra_actual)

                        while True:
                            status_orden = input(
                                "\n" + "Escriba '1' para continuar agregando "
                                f"productos, '2' para eliminar un producto, "
                                f"o '0' para finalizar su orden: "
                                )
                            
                            if status_orden == "1":
                                break

                            # Terminar proceso de compra y pasar a pago
                            elif status_orden == "0":
                                orden_compra_actual.estado = "Pendiente Pago" 
                                print(
                                    "\n" + "Orden lista para pago, "
                                    f"por favor agregue su metodo de pago")
                                break
                        
                            # Eliminar producto de la orden de compra
                            elif status_orden == "2":
                                id_producto_a_eliminar = input(
                                    "\n" + "Ingrese el ID del producto que "
                                    f"desea eliminar de su orden: ").upper()
                                
                                proceso_orden(orden_compra_actual, 
                                              id_producto_a_eliminar)
                            
                            
                                                
                # Desde catalogo , regresar a menu cliente loggeado
                elif opcion_orden == "2":
                    break

                else:
                    opcion_invalida()
                    continue

                if orden_compra_actual.estado == "Pendiente Pago":
                    break

        # Asignar metodo de pago a la orden de compra y finalizar la orden
            while orden_compra_actual.estado == "Pendiente Pago":

                print("\n" + "Eliga su método de pago")
                print("1. Tarjeta de crédito")
                metodo_pago_seleccionado = input("\n" + "Seleccione una opción: ")

                if metodo_pago_seleccionado == "1":
                    numero_tarjeta = input(
                        "Ingrese el número de su tarjeta de crédito: "
                        )
                    fecha_expiracion = input(
                        "Ingrese la fecha de expiración de su tarjeta (MM/AA): "
                        )
                    codigo_seguridad = input(
                        "Ingrese el código de seguridad de su tarjeta: "
                        )
                    
                    tarjeta= TarjetaCredito(numero_tarjeta,  
                                            fecha_expiracion, codigo_seguridad) 
                    
                    orden_compra_actual.agregar_metodo_pago(tarjeta)
                    print("\n" + f"Pago realizado con éxito, "
                          f"su orden {orden_compra_actual.id_orden} "
                          f"ha sido finalizada")
                    ordenes_compra.append(orden_compra_actual)

                    orden_compra_actual.actualizar_inventario(inventario) 

                    break
                else:
                    opcion_invalida()
                    continue
                    

        # Ver ordenes de compra del cliente loggeado
        elif opcion_cliente_loggeado == "2":
            cliente_actual.mostrar_ordenes_compra() 
            
            if cliente_actual.ordenes_compra: 

                while True:
                    print("\n" + "Presione '1' para eliminar una "
                          f"orden de compra, o '0' para regresar al "
                          f"menú anterior")
                    opcion_eliminar_orden = input(
                        "\n" + "Seleccione una opción: "
                        )
            
                    # Ruta para eliminar orden de compra
                    if opcion_eliminar_orden == "1":
                        id_orden_a_eliminar = input(
                            "\n" + "Ingrese el ID de la orden que "
                            f"desea eliminar: "
                            ).upper()

                        orden_a_eliminar = None
                        for orden in cliente_actual.ordenes_compra: 
                            if orden.id_orden == id_orden_a_eliminar:
                                orden_a_eliminar = orden
                                break

                        if orden_a_eliminar is None:
                            print("\n" + "No se encontró una "
                            f"orden con ese ID, por favor intente de nuevo")
                            continue

                        if orden_a_eliminar.estado == "Enviada":
                            print("\n" + "No se puede eliminar una "
                            f"orden que ya ha sido enviada, por favor "
                            f"intente de nuevo")
                            continue
                        else:
                            orden_a_eliminar.devolver_a_inventario(inventario) 
                            cliente_actual.borrar_orden_compra(id_orden_a_eliminar) 

                            if orden_a_eliminar in ordenes_compra:
                                ordenes_compra.remove(orden_a_eliminar)

                            print("\n" + f"Orden {id_orden_a_eliminar} "
                                  f"cancelada y productos devueltos al inventario")
                        

                    elif opcion_eliminar_orden == "0":
                        break
                    else:
                        opcion_invalida()
                        continue
            else:
                continue

        # Administrar quejas del cliente 
        elif opcion_cliente_loggeado == "3":
            # Si no tiene quejas registradas
            if not cliente_actual.quejas: # type: ignore
                print("\n" + "No tiene quejas registradas")
            # Si tiene quejas registradas
            else:
                cliente_actual.mostrar_quejas() # type: ignore

            while True:
                print("\n" + "Presione '1' para registrar una nueva queja, "
                      f"o '0' para regresar al menú anterior")
                opcion_queja = input("\n" + "Seleccione una opción: ")
                    
                # Ruta para registrar nueva queja
                if opcion_queja == "1":
                    while True:
                        descripcion_queja = input(
                            "\n" + "Ingrese la descripción de su queja: "
                            )
                        if descripcion_queja.strip():
                            break
                        print("\n" + "La descripción de la queja no "
                        f"puede estar vacía")
                    while True:
                        id_orden_queja = input("Ingrese el ID de la orden " 
                        f"relacionada con su queja (opcional): ").upper()

                        #Si no ingresa ID , se asigna un none 
                        if id_orden_queja == "":
                            id_orden_queja = None

                        #busqueda de queja para ver si coincide con existente
                        orden_encontrada = False
                        if id_orden_queja is not None:
                            for orden in cliente_actual.ordenes_compra: 
                                if orden.id_orden == id_orden_queja:
                                    orden_encontrada = True
                                    break
                            if not orden_encontrada:
                                print(
                                    "\n" + "No se encontró una orden con ese "
                                    f"ID, intente de nuevo o presione Enter "
                                    f"para registrar la queja sin un ID de "
                                    f"orden asociado")
                                id_orden_queja = None
                                continue
                        #Registro de queja
                        ultima_q = cliente_actual.crear_queja(
                            descripcion_queja, 
                            id_orden_queja  # type: ignore
                            ) 
                        quejas.append(ultima_q) 
                        break

                # Ruta para regresar al menu anterior
                elif opcion_queja == "0":
                    break
                else:
                    opcion_invalida()
                    continue

        #Administrar suscripcion a catalogo
        elif opcion_cliente_loggeado == "4":
            #Ruta si no tiene suscripcion activa
            if cliente_actual.suscripcion is None: 
                while True:
                    print("\n" + "No tienes una suscripción activa, Presiona "
                          f"'1' para recibir el catalogo mensualmente y '0' "
                          f"para regresar al menú anterior")
                    opcion_suscripcion = input("\n" + "Seleccione una opción: ")

                    if opcion_suscripcion == "1":
                        cliente_actual.activar_suscripcion()
                        break
                    
                    elif opcion_suscripcion == "0":
                        break

                    else:
                        opcion_invalida()
                        continue
            
            # Ruta si tiene suscripcion activa 
            elif cliente_actual.suscripcion.status == "Activa": 
                while True:
                    print("\n" + "Ya tienes una suscripción activa, si "
                          f"deseas cancelar tu suscripcion presiona '1', "
                          f"para regresar al menú anterior presiona '0'")
                    opcion_suscripcion_activa = input(
                        "\n" + "Seleccione una opción: "
                        )
                    # Cancelacion Suscripcion
                    if opcion_suscripcion_activa == "1":
                        cliente_actual.cancelar_suscripcion() 
                        break
                    # Regresar menu anterior
                    elif opcion_suscripcion_activa == "0":
                        break

                    else:
                        opcion_invalida()
                        continue
            
            # Ruta si tiene suscripcion cancelada
            elif cliente_actual.suscripcion.status == "Cancelada": 
                while True:
                    print("\n" + "Tu suscripción está cancelada, si deseas "
                          f"reactivar tu suscripcion presiona '1', para "
                          f"regresar al menú anterior presiona '0'")
                    opcion_suscripcion_cancelada = input(
                        "\n" + "Seleccione una opción: "
                        )
                    # Reactivar Suscripcion
                    if opcion_suscripcion_cancelada == "1":
                        cliente_actual.activar_suscripcion() 
                        break
                    # Regresar menu anterior
                    elif opcion_suscripcion_cancelada == "0":
                        break

                    else:
                        opcion_invalida()
                        continue
                
        # Cierre Sesion Cliente
        elif opcion_cliente_loggeado == "0":
            print("\n" + "Cerrando sesión...")
            return

def menu_gerente(empleado_actual : GerenteRP, quejas : list) -> None:
    while True:
        print("\n" + f"Bienvenido, {empleado_actual.cargo} "
              f"{empleado_actual.nombre_completo}!") 
        print("\n" + "Estas son las quejas registradas en el sistema:")
        if quejas:
            empleado_actual.mostrar_quejas(quejas) # type: ignore
        else:
            print("\n" + "No hay quejas registradas en el sistema")

        print("\n" + "Presione '0' para cerrar sesión")
        opcion_cerrar_sesion = input("\n" + "Seleccione una opción: ")
        
        if opcion_cerrar_sesion == "0":
                    print("\n" + "Sesion cerrada")
                    return
        else:
                    opcion_invalida()
                    continue

def menu_agente(empleado_actual : AgenteDeposito,
                ordenes_compra : list[OrdenCompra],
                transportistas : list[EmpresaTransporte],
                inventario : Inventario) -> None:
    while True:
    # Menu Agente de Deposito
        print("\n" + "----- MENU AGENTE -----")
        print("Seleccione una de las siguientes opciones")   
        print("1. Ver órdenes de compra")
        print("2. Alistar pedidos para envío")
        print("0. Cerrar sesión")

        opcion_agente = input("\n" + "¿Que desea hacer?: ")

        # Ver ordenes de compra
        if opcion_agente == "1":
            if ordenes_compra:
                for orden in ordenes_compra:
                    print(orden)
            else:
                print("\n" + "No hay órdenes de compra registradas en el sistema")
    
        # Alistar pedidos para envío
        elif opcion_agente == "2":

            while True:
                id_orden_a_alistar = input(
                    "\n" + "Ingrese el ID de la orden que desea alistar "
                    f"para envío o presione '0' para regresar al menú "
                    f"anterior: ").upper()

                if id_orden_a_alistar == "0":
                    break
                
                orden_a_alistar = None
                for orden in ordenes_compra:
                    if orden.id_orden == id_orden_a_alistar:
                        orden_a_alistar = orden
                        break
                
                if orden_a_alistar is None:
                    print("\n" + "No se encontró una orden "
                          f"con ese ID, por favor intente de nuevo")
                    continue

                print("\n" + "Seleccione la empresa de "
                      f"transporte para el envío:")
                for idx, transportista in enumerate(transportistas):
                    print(f"{idx + 1}. {transportista.nombre}")
                
                opcion_transportista = input("\n" + "Seleccione una opción: ")

                if opcion_transportista not in [
                    str(i) for i in range(1, len(transportistas) + 1)
                    ]:
                    opcion_invalida()
                    continue

                transportista_seleccionado = transportistas[
                    int(opcion_transportista) - 1
                    ]
                empleado_actual.alistar_orden_para_envio(
                    orden_a_alistar, transportista_seleccionado
                    )
        
        elif opcion_agente == "0":
            print("\n" + "Sesion cerrada")
            return
        else:
            opcion_invalida()
            continue
                
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
                        print("\n" + "Correo no encontrado, "
                        f"por favor intente de nuevo")

        # Volver al menú principal
        elif opcion_cliente == "3":
            continue
        else:
            opcion_invalida()
            continue

        # Desde aqui sigue la logica de un cliente loggeado
        print("\n" + 
              f"Bienvenido, {cliente_actual.nombre} " # type: ignore
              f"{cliente_actual.apellido}!")     # type: ignore

        #menu para cliente loggeado
        menu_cliente_loggeado(cliente_actual, catalogo, # type: ignore
                              inventario, ordenes_compra, 
                              quejas, transportistas) # type: ignore
        login = False
        cliente_actual = None

    # Portal Empleados 
    elif opcion_portal == "2":
        print("\n" + "Bienvenido al Portal de Empleados")
        print("\n" + "Por favor inicie sesión para continuar")
        
        # Login Empleado Registrado
        empleado_actual = None
        while not login: 
                    usuario= input("Ingrese su  usuario:")
                    contraseña = input("Ingrese su contraseña: ")
                    encontrado = False
                    for e in empleados:
                        if e.usuario == usuario and e.contraseña == contraseña:
                            empleado_actual = e
                            login = True
                            encontrado = True
                            break
                    if not encontrado:
                            print("\n" + "Credenciales no encontradas, "
                            f"por favor intente de nuevo")

        # Ruta para gerente 
        if empleado_actual.cargo == "Gerente": # type: ignore
            print("\n" + f"Bienvenido {empleado_actual.cargo} " # type: ignore
                  f"{empleado_actual.nombre_completo}!") # type: ignore
            menu_gerente(empleado_actual, quejas) # type: ignore
            login = False
            empleado_actual = None
            
                
        # Ruta para agente de deposito
        elif empleado_actual.cargo == "Agente": # type: ignore
            print("\n" + f"Bienvenido {empleado_actual.cargo} " # type: ignore
                  f"{empleado_actual.nombre_completo}!") # type: ignore
            menu_agente(empleado_actual, ordenes_compra, # type: ignore
                        transportistas, inventario) # type: ignore
            login = False
            empleado_actual = None
            
    else:
        opcion_invalida()
        