import os
import shutil
import send2trash

archivo = open('curso.txt','w')
archivo.write("Esto es una prueba")
archivo.close()

shutil.move('curso.txt', 'c:\\users\\david\\desktop\\archivo.txt')
send2trash.send2trash('c:\\users\\david\\desktop\\archivo.txt')

print(os.listdir())


