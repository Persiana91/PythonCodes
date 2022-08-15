import os
from pathlib import Path, WindowsPath


def Bienvenida():
    print("Bienvenido a Código receta")


def menu():
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoria")
    print("4. Eliminar receta")
    print("5. Eliminar categoria")              #REPARAR
    print("6. Salir")
    return input("Ingresa una opción: ")


def mostrar_recetas(ruta):
    recetas = Path(ruta).glob("**/*.txt")
    cantidad_recetas = 0
    print("Lista de recetas\n----------------------------")
    for receta in recetas:
        print(receta.stem)
        cantidad_recetas += 1
    print(f"\nHay {cantidad_recetas} recetas")


def ver_receta(ruta):
    ruta = Path(ruta)
    f = open(ruta,'r')
    res = f.read()
    f.close()
    return res


def crear_receta(ruta, receta):
    ruta = Path(ruta)
    f = open(ruta,'w')
    f.write(receta)
    f.close()


def crear_categoria(ruta,categoria):
    ruta = WindowsPath(Path(ruta,categoria))
    Path.mkdir(ruta)


def eliminar_receta(ruta,categoria,receta):
    ruta = Path(ruta,categoria,receta + '.txt')
    ruta.unlink()


def eliminar_categoria(ruta,categoria):
    recetas = Path(ruta).glob('**/*.txt')
    for x in recetas:
        eliminar_receta(ruta,categoria,x)
    Path(ruta,categoria).rmdir()


rutarecetas = Path(Path.home(),Path().resolve(),"Recetas")

Bienvenida()
opcion = 0
while opcion != '6':
    mostrar_recetas(rutarecetas)
    opcion = menu()
    match opcion:
        case '1':
            categoria = input("Ingresa la categoria de la receta: ")
            receta = input("ingresa el nombre de la receta: ")
            if Path(rutarecetas,categoria).exists() == False:
                print("La categoría no existe")
            elif Path(rutarecetas,categoria,receta + ".txt").exists() == False:
                print("No existe la receta")
            else:
                ruta = Path(rutarecetas,categoria,receta + ".txt")
                print(ver_receta(ruta))

        case '2':
            categoria = input("Ingresa la categoria de la receta: ")
            if Path(rutarecetas,categoria).exists() == False:
                print("La categoría no existe")
            else:
                receta = input("Nombre de la receta: ")
                contenido = input("Contenido de la receta: ")
                crear_receta(Path(rutarecetas,categoria,receta + ".txt"),contenido)

        case '3':
            categoria = input("Ingresa la categoria de la receta: ")
            if Path(rutarecetas, categoria).exists() == True:
                print("La categoría ya existe")
            else:
                crear_categoria(rutarecetas,categoria)
        case '4':
            receta = input("Ingresa el nombre de la receta: ")
            categoria = input("Ingresa la categoria de la receta: ")
            if not Path(rutarecetas, categoria).exists():
                print("La categoría no existe")
            elif not Path(rutarecetas, categoria, receta + ".txt").exists():
                print("No existe la receta")
            else:
                eliminar_receta(rutarecetas,categoria,receta)
        case '5':
            categoria = input("Ingresa la categoria de la receta: ")
            if not Path(rutarecetas, categoria).exists():
                print("La categoría no existe")
            else:
                eliminar_categoria(rutarecetas, categoria)
    input("Pulsa Enter para continuar")
    os.system('cls')