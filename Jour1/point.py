class Point:
    def __init__(self):
        self.x = 4
        self.y = 8

    def afficherLesPoints(self):
        print(f"x: {self.x}\ny: {self.y}\n")
    
    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

coordonnee = Point()

coordonnee.afficherLesPoints()
coordonnee.changerX(9)
coordonnee.changerY(34)
coordonnee.afficherLesPoints()