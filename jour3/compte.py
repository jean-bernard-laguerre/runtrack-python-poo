class CompteBancaire:
    def __init__(self, num, nom, prenom, solde):
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def getSolde(self):
        return self.__solde
    def setSolde(self, solde):
        self.__solde = solde

    def afficher(self):
        print(f"Numero: {self.__num}")
        print(f"Nom: {self.__nom}")
        print(f"Prenom: {self.__prenom}")
    
    def afficherSolde(self):
        print(f"Solde {self.__nom}: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):

        if self.__solde > montant or self.__decouvert:
            self.__solde -= montant
        else:
            print("Solde insuffisant")
        self.agios()
        self.afficherSolde()

    def virement(self,montant, compte):

        if self.__solde > montant  or self.__decouvert:
            self.__solde -= montant
            compte.versement(montant)
        else:
            print("Solde insuffisant")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= (-self.__solde*.07)


compte1 = CompteBancaire("186651", "Doe", "John", 9000)
compte2 = CompteBancaire("186651", "Dupont", "Jean", -2000)

compte1.afficherSolde()
compte2.afficherSolde()

compte2.retrait(400)
compte1.virement(3000, compte2)

compte1.afficherSolde()
compte2.afficherSolde()

compte1.retrait(4000)
compte1.afficherSolde()

