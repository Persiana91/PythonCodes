from pathlib import Path, PureWindowsPath

#Lo entiende Mac, Linux y Windows, a diferencia de la librería OS

carpeta = Path('c:/prueba')
archivo = carpeta / 'otro.txt'
windows = PureWindowsPath(carpeta)

f = open(archivo,'r')
print(f.read())
f.close()

print(archivo.read_text())
print(windows)

for txt in Path(windows).glob("*.txt"):
    print(txt)