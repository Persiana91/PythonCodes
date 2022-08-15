def reducir_lista(lista):
    lista = set(lista)
    lista.remove(max(lista))

    return promedio(lista)


def promedio(lista):
    lista=list(lista)
    return sum(lista)/len(lista)


lista_numeros = [1,5,2,5,3,2,7,9,2,9,4]
print(reducir_lista(lista_numeros))