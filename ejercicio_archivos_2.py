f = open('mi_archivo.txt','a')
f.write("Nuevo inicio de sesión")
f.close
f = open('mi_archivo.txt','r')
print(f.read())
f.close