class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro','tucan')

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
print(Pajaro.alas)