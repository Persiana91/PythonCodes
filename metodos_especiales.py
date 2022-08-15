class CD:

    def __init__(self,autor):
        self.autor = autor

    def __len__(self):              # Actuador sobre len() en la clase cD, método especial
        return len(self.autor)

mi_CD = CD('rammstein')
print(len(mi_CD))
del mi_CD
print(len(mi_CD))       # Error, se ha eliminado la instancia