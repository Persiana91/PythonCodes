from random import choice

def lanzar_moneda():
    res = choice(["Cara","Cruz"])
    probar_suerte(res,lista_numeros)

def probar_suerte(resultado_lanzamiento,lista):
    if resultado_lanzamiento == "Cara":
        print("La lista se autodestruirá")
        lista.clear()
    else:
        print("La lista fue salvada")


lista_numeros = [1,5,2,5,3,2,7,9,2,9,4]
lanzar_moneda()