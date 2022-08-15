class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio")

    def volar(self,metros):
        print("El pajaro volo {} metros".format(metros))
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print("El pajaro es {}".format(self.color))

    @classmethod
    def huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")

pajaro = Pajaro('amarillo','canario')

pajaro.volar(50)

Pajaro.huevos(4)    # Esto no es una instancia, classmethod