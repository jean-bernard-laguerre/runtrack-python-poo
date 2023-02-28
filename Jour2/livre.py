class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def setTitre(self, titre):
        self.__titre = titre
    def setAuteur(self, auteur):
        self.__auteur = auteur
    def setPages(self, pages):

        if type(pages) is int and pages > 0:
            self.__pages = pages
        else:
            print("Le nombre de page doit etre un entier positif")
            
    def getTitre(self):
        return self.__titre 
    def getAuteur(self):
        return self.__auteur
    def getPages(self):
        return self.__pages
       
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("le livre n'est pas disponible.")
    def rendre(self):
        if self.verification():
            print("le livre n'a pas été emprunté.")
        else:
            self.__disponible = True

livre1 = Livre("test", "Auteur", 150)
print(livre1.getPages())
livre1.setPages(-65)
livre1.setPages(948)
print(livre1.getPages())

livre1.rendre()
livre1.emprunter()
livre1.emprunter()
livre1.rendre()
