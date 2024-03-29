import funciones.clientes as c
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
    c.cf.checkFile(c.clientes)
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
                os.system('cls')
                title = """
                +++++++++++++++++++++++++++++
                + CREACION DE NUEVO CLIENTE +
                +++++++++++++++++++++++++++++
                """
                print(title)
                cliente={
                    'cc':'00',
                    'nombre':'',
                    'apellido':'',
                    'emailpersonal':'',
                    'emailcorporativo':'',
                    'edad':0
                }
                for key,item in cliente.items():
                    if (key != 'edad'):
                        cliente[key] = input(f'Ingrese {key.capitalize()} del Cliente : ')
                    else:
                        validateAge = True
                        while (validateAge):
                            try:    
                                cliente['edad'] = input(f'Ingrese {key.capitalize()} del Cliente : ')
                            except ValueError:
                                print('El valor ingresado es invalido')
                            else:
                                validateAge = False
                isAddPhone = True
                telefono = {
                    'telefono':[]
                }
                phone = {
                    'titulo' : 'xx',
                    'valor' : ''
                }
                while (isAddPhone):
                    phone['titulo'] = input('Ingrese ubicacion (Casa,oficina,Movil) : ')
                    phone['valor']= input(f'Ingrese el Nro {phone['titulo']} del Cliente {cliente['nombre']} : ')
                    telefono['telefono'].append(phone)
                    isAddPhone = bool(input('Para terminar presiona Enter.... o Cualquier letra para continuar'))
                cliente.update(telefono)
                os.system('cls')
                print(cliente)
                os.system('pause')
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