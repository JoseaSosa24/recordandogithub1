
print("Departamento de confección")
print("1. Ingresar producto a fabrica")
print("2. Mostrar inventario en fabrica")
print("0. SALIR")

opcion =1
listaProductos=[]
while opcion!=0:
    opcion =int (input("digita una opción: "))
    producto=input("Digita el producto que ingresa a fabricación: ")
    #agregar producto a la lista
    listaProductos.append(producto)
    if opcion==1:
        print("vamos a ingrear un nuevo producto: ")
    elif opcion==2:
        print("mostrando el inventraio")
    elif opcion==0:
        print("gracias, hasta pronto")
    else:
        print("opcion invalida..")
        
print("adios, fin del programa")    