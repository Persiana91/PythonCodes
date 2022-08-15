def cantidad_pares(lista):
    suma = 0
    for n in range(len(lista)):
        if lista[n]%2==0:
            suma += 1
    return suma

lista_numeros = [2,5,8,16,47,938]
print(cantidad_pares(lista_numeros))