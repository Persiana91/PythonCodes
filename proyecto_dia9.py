import os, re
from datetime import datetime

# 'proyecto dia 9\Mi_Gran_Directorio'
from pathlib import Path


nArchivos = []


def leerarchivo(ruta):
    f = open(ruta,'r')
    res = f.read()
    f.close()
    patron = r'N\D{3}-\d{5}'
    resultado = re.search(patron, res)
    if resultado:
        nArchivos.append((resultado.group()))


def recorrer(directorio):
    cont = 0
    for nombre_directorio, dirs, ficheros in os.walk(directorio):
        for file in ficheros:
            leerarchivo(Path(nombre_directorio,file))


tiempoinicio = datetime.now().microsecond
ruta = 'proyecto dia 9/Mi_Gran_Directorio'
recorrer(ruta)
print("Códigos serie: \n---------------")
for x in range(len(nArchivos)):
    print("Código {}:\t{}".format(x,nArchivos[x-1]))
print("Se han encontrado {} archivos.".format(len(nArchivos)))
tiempofin = datetime.now().microsecond
tiempoms = tiempofin - tiempoinicio
tiempo = tiempoms / 1000
print("La ejecución ha durado {}ms {}s".format(tiempoms, tiempo))