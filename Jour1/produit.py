class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prixHT = prix
        self.TVA = .2

    def CalculerPrixTTC(self):
        return self.prixHT + (self.prixHT * self.TVA)
    
    def changerNom(self, nom):
        self.nom = nom

    def changerPrix(self, prix):
        self.prixHT = prix

    def afficherInfos(self):
        print(f"Nom: {self.nom}\nPrix: {self.prixHT} €\nPrix TTC: {self.CalculerPrixTTC()} €\n")

produit1 = Produit("Fromage", 6)
produit1.afficherInfos()
produit1.changerPrix(9)
produit1.changerNom("Fromage frais")
produit1.afficherInfos()