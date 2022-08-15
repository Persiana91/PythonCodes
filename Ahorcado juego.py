import sys
from random import randint

def pedir_letra():
    return input("Introduce una letra")

def validar_letra(txtoculto,letra,palabra):
    txtoculto = list(oculto)
    for x in range(len(palabra)):
        if letra == palabra[x]:
            txtoculto[x] = letra
    if palabra.find(letra) > -1:
        acertado = True
    else:
        acertado = False
    return txtoculto,acertado


def generar_palabra():
    palabras = ['gato','perro','ciervo','pantera']
    return palabras[randint(0,len(palabras)-1)]


def comprobar_fin(oculto):
    fin = True
    for x in range(len(oculto)):
        if oculto[x] == '_':
            return False
    return True


oculto = ''
palabra = generar_palabra()
vidas = 6
for x in range(len(palabra)):
    oculto += '_'
while vidas > 0:
    print(' '.join(oculto))
    letra = pedir_letra()
    oculto,acertado = validar_letra(oculto,letra,palabra)
    if acertado == False:
        vidas -= 1
    print(' '.join(oculto))
    if comprobar_fin(oculto) == True:
        print("Has ganado, texto descifrado")
        sys.exit(0)
    print("Vidas: {}".format(vidas))
print("¡Ahorcado!")
sys.exit(0)