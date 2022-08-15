class Padre:
    def Hablar(self):
        print("Hola")

class Hijo(Padre):
    pass

class Nieto(Hijo):
    pass


mi_niieto = Nieto()
mi_niieto.Hablar()