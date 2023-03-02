import random

class Carte:
    def __init__(self, couleur, signe, valeur):
        self.couleur = couleur
        self.valeur = valeur
        self.signe = signe

class Joueur:
    def __init__(self):
        self.main = []

    def score(self):
        points = 0

        for carte in self.main:

            if carte.valeur <= 10:
                points += carte.valeur

            elif carte.valeur > 10:
                points += 10

        return points
    
class Jeu:
    def __init__(self):

        self.remplirPaquet()
        self.joueur = Joueur()
        self.croupier = Joueur()
        self.lancerJeu()

    def donnerCarte(self, joueur):

        carte = random.randint(0, len(self.paquet)-1)
        joueur.main += [self.paquet[carte]]
        self.paquet.pop(carte)  
    
    def remplirPaquet(self):
        self.paquet = []

        for x in range(4):
            for y in range(1, 13):
                match x:
                    case 0:
                        self.paquet += [Carte("Noir", "Pique", y)]
                    case 1:
                        self.paquet += [Carte("Rouge", "Coeur", y)]
                    case 2:
                        self.paquet += [Carte("Noir", "Trefle", y)]
                    case 3:
                        self.paquet += [Carte("Rouge", "Carreau", y)]

    def lancerJeu(self):
        
        for i in range(2):
            self.donnerCarte(self.joueur)
            self.donnerCarte(self.croupier)

        while True:

            print("Joueur: ", self.joueur.score())
            print("Croupier: ", self.croupier.score())

            choix = input("Prendre une carte? Oui(0): ")

            if self.croupier.score() < 17:
                self.donnerCarte(self.croupier)

            if choix == "0":
                self.donnerCarte(self.joueur)
            
            if (choix != "0" or self.joueur.score() > 21) and self.croupier.score() >= 17:
                
                if self.joueur.score() > 21 or self.croupier.score() == 21:
                    print("Defaite")
                
                elif self.joueur.score() > self.croupier.score() or self.croupier.score() > 21:
                    print("Victoire")

                else:
                    print("Egalité")

                break

Jeu()