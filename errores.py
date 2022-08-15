def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    #print(n1+n2 + "aa")
    print(n1+n2)


try:
    suma()
except TypeError:
    print("Error de tipado")
except ValueError:
    print("Error de valor")
else:
    print("Todo bien")
finally:
    print("Eso fué la comprobacion")