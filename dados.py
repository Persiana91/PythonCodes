from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1, 6)

    evaluar_jugada(dado1,dado2)

    return dado1,dado2


def suma(a,b):
    return a+b


def evaluar_jugada(dado1,dado2):
    suma_dados = suma(dado1,dado2)
    if suma(dado1,dado2) <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma(dado1,dado2) >6 and suma(dado1,dado2)<10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma(dado1,dado2) >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


dado1,dado2=lanzar_dados()
print(dado1)
print(dado2)