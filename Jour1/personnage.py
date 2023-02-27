class Personnage:
    def __init__(self):
        self.x = 2
        self.y = 8

    def position(self):
        return (self.x, self.y)

    def haut(self):
        self.x -= 1

    def bas(self):
        self.x += 1

    def droite(self):
        self.y += 1

    def gauche(self):
        self.y -= 1

perso = Personnage()

print(f"Position: {perso.position()}")
perso.haut()
perso.gauche()
print(f"Position: {perso.position()}")