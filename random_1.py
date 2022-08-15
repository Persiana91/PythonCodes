from random import *

print(randint(1,100))

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

#Mezclar
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)