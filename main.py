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

                # Menu en vista de catalogo
                print("\n" + "¿Que desea hacer?")
                print("1. Realizar una orden de compra")
                print("2. Volver al menú anterior")
                opcion_orden = input("\n" + "Seleccione una opción: ")

                if opcion_orden == "1":
                    cliente_actual.crear_orden_compra()

                # Desde catalogo , regresar a menu cliente loggeado
                if opcion_orden == "2":
                    continue

                # Cierre Sesion Cliente
                if opcion_cliente_loggeado == "0":
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