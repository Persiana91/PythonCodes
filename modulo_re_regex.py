"""
    Expresiones regulares
    \d Digito
    \w Alfanumerico
    \s Espacio en blanco
    \D No es un dígito
    \W No es alfanumerico
    \S No es un espacio
    Cuantificadores: {veces Repetido}
"""

import re

texto = 'el telefono es 000-222-1133 prueba'

patron = r'\d{3}-\d{3}-\d{4}'

busqueda = re.search(patron, texto)

print(busqueda.group())
