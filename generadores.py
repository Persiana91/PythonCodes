def mi_funcion():
    return 4


def mi_generador():
    for x in range(1,5):
        yield x*10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))