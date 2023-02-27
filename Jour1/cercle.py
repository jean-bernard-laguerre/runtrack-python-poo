import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon

    def circonference(self):
        return 2 * self.rayon * math.pi
    
    def aire(self):
        return self.rayon**2 * math.pi
    
    def diametre(self):
        return self.rayon*2
    
    def afficherInfos(self):
        print(f"Rayon: {self.rayon}\nCirconférence: {self.circonference()}\nAire: {self.aire()}\nDiametre: {self.diametre()}\n")
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)
cercle1.afficherInfos()
cercle2.afficherInfos()