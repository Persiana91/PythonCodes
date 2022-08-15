import sys
from random import randint

nombre = input("¿Cómo te llamas? ")
aleatorio = randint(1,100)
for i in range(0,8):
    num_usuario = int(input("Hola {}, indica un número del 1 al 100: ".format(nombre)))
    if num_usuario == aleatorio:
        print("¡Acertaste el número {} en el intento {}!".format(aleatorio,i))
        sys.exit(0)
    if num_usuario<0 or num_usuario>100:
        print("Número fuera de rango")
    if aleatorio<num_usuario:
        print("El valor pensado es menor")
    if aleatorio>num_usuario:
        print("El valor pensado es mayor")

print("¡Fallaste! El número era el {}.".format(aleatorio))