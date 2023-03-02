import math

class Forme:
    def __init__(self):
        pass
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, long, large):
        self.__longueur = long
        self.__largeur = large
        Forme.__init__(self)

    def perimetre(self):
        return (self.__longueur + self.__largeur)*2

    def aire(self):
        return self.__longueur * self.__largeur


    def getLongueur(self):
        return self.__longueur
    def getLargeur(self):
        return self.__largeur
    def setLongueur(self, long):
        self.__longueur = long
    def setLargeur(self, large):
        self.__largeur = large


class Cercle(Forme):
    def __init__(self, rad):
        Forme.__init__(self)
        self.radius = rad

    def aire(self):
        return self.radius**2 * math.pi

class Parallelepipede(Rectangle):
    def __init__(self, long, large, hauteur):
        Rectangle.__init__(self, long, large)
        self.hauteur = hauteur

    def volume(self):
        return self.aire() * self.hauteur 
    
rect = Rectangle(9, 6)
print("Perimetre: ", rect.perimetre())
print("Aire: ", rect.aire())

rond = Cercle(6)
print("Aire: ", rond.aire())

para = Parallelepipede(4, 8, 3)
print("Volume: ", para.volume())

