palabra = "Curso"


def invertir_palabra(palabra):
    palabra = palabra.upper()
    return ''.join(reversed(palabra))


print(invertir_palabra(palabra))