from compras import OrdenCompra
from personas import Cliente

clientes = []

# main.py
def menu_usuario():
    print("\n" + "----- TeleVentas -----")
    print("1. Portal Clientes")
    print("2. Portal Empleados")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    direccion = input("Ingrese su dirección: ")
    correo = input("Ingrese su correo electrónico: ")
    print("\n" + f"{nombre} , has sido registrado exitosamente")
    return Cliente(nombre, apellido, direccion, correo)

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

        # Usuario Nuevo
        if opcion_cliente == "1":
            print("\n" + "Por favor regístrese para continuar")
            cliente = crear_cliente()
            # añadir cliente a la lista de clientes registrados
            clientes.append(cliente)

        elif opcion_cliente == "2":
            print("\n" + "Por favor inicie sesión para continuar")
            # lógica de inicio de sesión

        elif opcion_cliente == "3":
            continue




    # Portal Empleados 
    elif opcion_portal == "2":
        print("\n" + "Bienvenido al Portal de Empleados")
        # lógica de crear orden
    else:
        print("\n" + "Opción Invalida, por favor seleccione una opción válida")

menu_usuario()