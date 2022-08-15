precios = [('cafe',0.5),('cafe 2',1.6),('cafe 3',2)]


def masalto(lista):
    precio_mayor = 0
    producto = ''

    for cafe,precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            producto = cafe
        else:
            pass

    return producto, precio_mayor


producto,precio = masalto(precios)
print("El producto {} vale {}€".format(producto, precio))