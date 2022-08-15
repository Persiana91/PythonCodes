mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

#¿Existe el valor 8?
print(8 in mi_set)

#Unir sets
mi_set2 = ([6,7,8,9])
set_total = mi_set.union(mi_set2)
print(set_total)
print(8 in set_total)

#Agregar elemento 10
set_total.add(10)
print(set_total)

#Eliminar elemento 8
set_total.remove(8)
print(set_total)

#Descartar, eliminar solo si existe, sino se omite
set_total.discard(15)
print(set_total)

#.pop() elimina un elemento aleatorio, peligroso
set_total.pop()
print(set_total)

#Limpiar contenido de un set
set_total.clear()
print(set_total)
print(type(set_total))