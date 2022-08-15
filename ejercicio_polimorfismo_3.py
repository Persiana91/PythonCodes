class Mago():
    @staticmethod
    def defender():
        print("Escudo mágico")

class Arquero():
    @staticmethod
    def defender():
        print("Esconderse")

class Samurai():
    @staticmethod
    def defender():
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

mag = Mago()
arq = Arquero()
samu = Samurai()
objetos = [arq,mag,samu]
for x in objetos:
    personaje_defender(x)