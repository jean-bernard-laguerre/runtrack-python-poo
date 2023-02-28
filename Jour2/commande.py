carte = [{"nom": "pates", "prix": 5},
         {"nom": "riz", "prix": 3},
         {"nom": "legume", "prix": 4},
         {"nom": "fruit", "prix": 2},
         {"nom": "soda", "prix": 2},
         {"nom": "eau", "prix": 1}]

def tva(prix):
    
    return (prix * .2)

class Commande:
    def __init__(self, num, plats):
        self.__num = num
        self.__plats = plats
        self.__statut = "En cours"

    def __total(self):

        total = 0
        for plat in self.__plats:
            total += plat["prix"] + tva(plat["prix"])

        return total

    def annuler(self):

        if self.__statut == "En cours":
            self.__statut = "Annulé"
        else:
            print("Commande déja terminée.")

    def ajouter(self, plat):

        if self.__statut == "En cours":
            self.__plats += [plat]
        else:
            print("Commande terminée ou annulée.")
    
    def afficheCommande(self):

        print(f"Commande n°: {self.__num}")

        for plat in self.__plats:
            print(plat["nom"])

        print(f"Total: {self.__total()} €")
    

commande1 = Commande("1684656", [carte[0], carte[4]])
commande1.ajouter(carte[2])

commande1.afficheCommande()
