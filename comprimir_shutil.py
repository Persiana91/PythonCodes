import shutil

carpeta_origen = "C:\\Users\\david\\Desktop\\CursoPython\\dia9\\Codigos"

archivo_destino = "dia9codigos"

shutil.make_archive(archivo_destino,"zip",carpeta_origen)