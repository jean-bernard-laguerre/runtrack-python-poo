class Tache:
    def __init__(self, titre, desc):
        self.__titre = titre
        self.__description = desc
        self.__statut = "A faire"

    def getTitre(self):
        return self.__titre
    def getDescription(self):
        return self.__description
    def getStatut(self):
        return self.__statut
    
    def setTitre(self, titre):
        self.__titre = titre
    def setDescription(self, desc):
        self.__description = desc
    def setStatut(self, statut):
        self.__statut = statut


class ListeDeTache:

    def __init__(self, taches):
        self.__taches = taches

    def getTaches(self):
        return self.__taches
    
    def ajouterTache(self, tache):
        self.__taches += [tache]

    def supprimerTache(self, cible):

        for i,tache in enumerate(self.__taches):
            if tache == cible:
                self.__taches.pop(i)
        else:
            print("tache introuvable")

    def marquerCommeFinie(self, tache):

        tache.setStatut("Terminé")

    def afficherListe(self):

        for tache in self.__taches:
            print(f"{tache.getTitre()}: {tache.getStatut()}")

    def filtreListe(self, statut):

        listeFiltre = []

        for tache in self.__taches:
            if tache.getStatut() == statut:
                listeFiltre += [tache]
        
        return listeFiltre
    

lessive = Tache("Lessive", "Faire la lessive")
vaiselle = Tache("Vaiselle", "Faire la vaiselle")
menage = Tache("Menage", "Faire la menage")
rdv = Tache("Rendez-Vous", "Aller au rendez-vous")


liste = ListeDeTache([lessive, menage, rdv])
liste.marquerCommeFinie(lessive)

liste.afficherListe()

for tache in liste.filtreListe("A faire"):
    print(tache.getTitre())

