class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez,Reptil,Ave,Mamifero):
    def __init__(self):
        Ave.tiene_pico = True
        Vertebrado.vertebrado = True
        Reptil.venenoso = False

animal = Ornitorrinco()
animal.poner_huevos()
animal.nadar()
animal.caminar()
animal.amamantar()