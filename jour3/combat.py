import random

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie
        self.__garde = False

    def getNom(self):
        return self.__nom
    def getVie(self):
        return self.__vie
    def getGarde(self):
        return self.__garde
    
    def setNom(self, nom):
        self.__nom = nom
    def setVie(self, vie):
        self.__vie = vie

    def attaquer(self, cible):
        self.__garde = False

        if not cible.getGarde():
            cible.setVie(cible.getVie()-1)
        else:
            self.__vie -= 1

    def defendre(self):
        self.__garde = True

    def soin(self):
        self.__garde = False
        self.__vie += 1

class Jeu:
    def __init__(self):
        self.__niveau = self.choisirNiveau()
        self.lancerJeu()

    def choisirNiveau(self):

        while True:
            try:
                niveau = int(input("Choisir un niveau: "))
                if 0 <= niveau <= 5:
                    break
            except:
                print("[0-5]")

        return niveau
    
    def lancerJeu(self):
        self.joueur1 = Personnage("Joueur1", 3)
        self.joueur2 = Personnage("Joueur2", 3 + self.__niveau)

        while True:

            try:
                actions = [0, 0]
                actions[0] = int(input("Attaque(0) | Defense(1) | Soin(2):"))
                actions[1] = random.choice([0,1,2])

                for i,action in enumerate(actions):

                    match action:
                        case 0:
                            if i == 0:
                                self.joueur1.attaquer(self.joueur2)
                            else:
                                self.joueur2.attaquer(self.joueur1)
                        case 1:
                            if i == 0:
                                self.joueur1.defendre()
                            else:
                                self.joueur2.defendre()
                        case 2:
                            if i == 0:
                                self.joueur1.soin()
                            else:
                                self.joueur2.soin()

                print(f"{self.joueur1.getNom()}: {self.joueur1.getVie()} vie(s)")
                print(f"{self.joueur2.getNom()}: {self.joueur2.getVie()} vie(s)")

                if self.joueur1.getVie() == 0:
                    print(f"{self.joueur2.getNom()} a gagné")
                    break
            
                if self.joueur2.getVie() == 0:
                    print(f"{self.joueur1.getNom()} a gagné")
                    break

            except:
                print("Input invalide")

                
jeu = Jeu()


