import zipfile

'''# Comprimir ZIP
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", 'w')
mi_zip.write("comprimir.py")
mi_zip.close()'''

# Descomprimir ZIP
mi_zip = zipfile.ZipFile("a.zip", 'r')
mi_zip.extractall("proyecto dia 9")
mi_zip.close()  