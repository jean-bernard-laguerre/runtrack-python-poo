class Voiture:
    def __init__(self, marque, modele, annee, km):

        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__reservoir = 50
        self.__km = km
        self.__enMarche = False

    def getMarque(self):
        return self.__marque
    def getModele(self):
        return self.__modele
    def getAnnee(self):
        return self.__annee
    def getKm(self):
        return self.__km
    def getEnMarche(self):
        return self.__enMarche
    
    def setMarque(self, marque):
        self.__marque = marque
    def setModele(self, modele):
        self.__modele = modele
    def setAnnee(self, annee):
        self.__annee = annee
    def setKm(self, km):
        self.__km = km
    def setEnMarche(self, enMarche):
        self.__enMarche = enMarche

    def verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__enMarche = True
        else:
            print("Reservoir vide")

    def arreter(self):
        self.__enMarche = False

voiture1 = Voiture("Peugeot", "206", "2004", 2400)
voiture1.demarrer()
print(voiture1.getEnMarche())