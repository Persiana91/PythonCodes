def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("----------------------")
        funcion(palabra)
        print("----------------------")

    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


@decorar_saludo
def minusculas(texto):
    print(texto.lower())


minusculas("PyThON")
