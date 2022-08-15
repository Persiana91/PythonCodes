import os

ruta = os.getcwd() #Get Current Working Directory, directorio actual
rutatotal = ruta + '\\archivo.txt'
dir = os.path.dirname(rutatotal)
archivo = os.path.basename(rutatotal)
print("Directorio {}\nArchivo {}\nDir: {}\nTotal: {}".format(ruta,archivo,dir,rutatotal))