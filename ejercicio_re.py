import re

def verificar_cp(cp):
    if re.search(r"\w{2}\d{4}",cp) != None
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

verificar_cp("Cd9283")