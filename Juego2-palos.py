from random import  shuffle
palos = ['-','--','---','----']

def mezclar(lista):
    shuffle(lista)
    return lista


def suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un número del 1 al 4")

    return int(intento)


def comprobar(lista, intento):
    if lista[intento - 1] == '-':
        print("Perdiste")
    else:
        print("Te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")


palos_mezclados = mezclar(palos)
seleccion = suerte()
comprobar(palos_mezclados,seleccion)