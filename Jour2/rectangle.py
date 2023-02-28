class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur
    
rect1 = Rectangle(10, 5)
print(rect1.getLongueur())
rect1.setLongueur(9)
print(rect1.getLongueur())



