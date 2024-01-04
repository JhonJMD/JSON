import funciones.corefile as cf
clientes={    
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
