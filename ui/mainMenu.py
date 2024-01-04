import os
opciones = ['Gestor Clientes', 'Gestor Proveedores', 'Gestor Productos', 'Salir']
opcionClientes = ['Nuevo Cliente', 'Borrar Cliente', 'Editar Cliente', 'Buscar Cliente', 'Menu Principal']
def generarMainMenu():
    header = """
    +++++++++++++++++++++++++++++++++
    + SISTEMA GESTOR DE INVENTARIOS +
    +++++++++++++++++++++++++++++++++
    """
    print(header)
    for i,item in enumerate(opciones):
        print(f'{(i+1)} - {item}')
def generarClienteMenu():
    isActiveCostumer = True
    header = """
    ++++++++++++++++++++++++++++++
    + ADMINISTRACION DE CLIENTES +
    ++++++++++++++++++++++++++++++
    """
    while (isActiveCostumer):
        os.system('cls')
        print(header)
        for i,item in enumerate(opcionClientes):
            print(f'{(i+1)} - {item}')
        try:
            op = int(input(':)_'))
        except ValueError:
            print('Error en el dato ingresado')
        else:
            if (op == 1):
                pass
            elif (op == 2):
                pass
            elif (op == 3):
                pass
            elif (op == 4):
                pass
            elif (op == 5):
                isActiveCostumer = False
            else:
                print("Opcion no esta disponible............")
                os.system('pause')