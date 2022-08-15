lista = ['j','r','s']
res = lista[0:]

#Agregar dato a Lista (Agregar datos "F"
res.append("F")

#Eliminar dato de lista en la posición 1 (posicion necesaria)
#Sin parámetro índice elimina el último valor de la lista
res.pop(1)

#Ordenamiento de la lista
res.sort()

#Invertir órden de lista
res.reverse()

print(res)