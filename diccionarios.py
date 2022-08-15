diccionario = {'color': 'rojo', 'marca': 'alfa'}

print(diccionario)

print("El coche de la marca {} es de color {}".format(diccionario['marca'], diccionario['color']))

diccionario2 = {'c1': ['a','b','c'], 'c2':['d','e','f']}
letra = diccionario2['c2'][1]
print(letra.upper())

print(diccionario2)
#Llaves en diccionario 2
print(diccionario2.keys())

#Valores en diccionario 2
print(diccionario2.values())

#Elementos en un diccionario
print(diccionario2.items())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad']='36'
mi_dic['ocupacion']='Editora'
mi_dic['pais'] = 'Colombia'

print(mi_dic)