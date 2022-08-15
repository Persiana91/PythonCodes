from collections import Counter, defaultdict, namedtuple, deque

numeros = [8, 8, 8, 5, 5, 5, 6, 6, 4, 3, 5, 5, 6, 45, 3, 4, 6, 4, 5, 5, 5]

print(Counter(numeros))
print(Counter(numeros).most_common())   # Imprimir lista de mas a menos frecuentes
print(Counter(numeros).most_common(2))  # Imprimir los dos más frecuentes

mi_dic = defaultdict(lambda: 'nada')        # Si la llave no existe, asigna el valor 'nada' al diccionario
mi_dic['uno'] = 'verde'
print(mi_dic['noexiste'])
print(mi_dic['uno'])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('david', 2.05, 91)

print(ariel[2])      # Mostrar valor de la tupla en el indice 0

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades[1])