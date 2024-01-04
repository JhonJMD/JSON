import funciones.corefile as cf
clientes={    
}
cliente={
    'cc':'00',
    'nombre':'',
    'apellido':'',
    'telefono':[],
    'emailpersonal':'',
    'emailcorporativo':'',
    'edad':0
}
telefono={
    'descripcion':'',
    'numero':'000'
}
cf.MY_DATABASE = "data/clientes.json"
def NewCustomer():
    pass

def validarArchivoClientes():
    if __name__=='__main__':
        if (cf.checkFile()):
            print("OK ")
        else:
            cf.NewFile(clientes)
