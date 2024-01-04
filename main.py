import funciones.clientes as c
# import funciones.corefile as cf
if __name__=='__main__':
    if (c.cf.checkFile(c.cf.MY_DATABASE)):
        print("OK ")
    else:
        print ("Error")