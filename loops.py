mi_lista = ['david','paco','antonio']

for i in range(0, len(mi_lista)):
    print("Hola, {}".format(mi_lista[i]))

dicc = {'c1':'a','c2':'ok'}

for a,b in dicc.items():
    print(a,b)

numero = 10

while numero > 5:
    print(numero)
    numero -= 1