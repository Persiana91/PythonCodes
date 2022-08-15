texto = "Esto es un texto de prueba"

resultado = texto[2:14:2].upper()
print("Mayusculas: " + resultado)

resultado = resultado.lower()
print("Misma secuencia pero en minusculas: " + resultado)

resultado = texto.split()
print(resultado)

resultado = " ".join(resultado)
print(resultado)

resultado = texto.find("es un")
print(resultado)

resultado = texto.replace("es un", "prueba")

print(resultado)