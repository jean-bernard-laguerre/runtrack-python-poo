class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")
    
    def demarrer(self):
        print("Attention je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Portes: {self.portes}", end ="\n\n")
    
    def demarrer(self):
        print("Attention je roule en voiture")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roues = 2

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Roues: {self.roues}", end ="\n\n")

    def demarrer(self):
        print("Attention je roule en moto")
        
voiture1 = Voiture("Mercedes", "Classe A", "2020", 18500)
voiture1.informationVehicule()

moto1 = Moto("Yamaha", "1200 Vmax", "1987", 4500)
moto1.informationVehicule()

voiture1.demarrer()
moto1.demarrer()