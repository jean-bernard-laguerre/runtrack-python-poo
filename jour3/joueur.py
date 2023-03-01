class Joueur:
    def __init__(self, nom, num, pos):

        self.__nom = nom
        self.__num = num
        self.__pos = pos
        self.__but = 0
        self.__passe = 0
        self.__crtJaune = 0
        self.__crtRouge = 0
    
    def marquerUnBut(self):
        self.__but += 1

    def effectuerUnePasseDecisive(self):
        self.__passe += 1

    def recevoirUnCartonJaune(self):
        self.__crtJaune += 1

    def recevoirUnCartonRouge(self):
        self.__crtRouge += 1

    def afficherStatistique(self):

        print(f"Nom: {self.__nom}")
        print(f"Numero: {self.__num}")
        print(f"Position: {self.__pos}")
        print(f"But: {self.__but}")
        print(f"Passe décisive: {self.__passe}")
        print(f"Carton jaune: {self.__crtJaune}")
        print(f"Carton rouge: {self.__crtRouge}")

class Equipe:
    def __init__(self, nom):

        self.__nom = nom
        self.__joueurs = []

    def ajouterJoueur(self, joueur):
        self.__joueurs += [joueur]

    def afficherStatistiquesJoueurs(self):

        for joueur in self.__joueurs:
            joueur.afficherStatistique()
            print("")

    def mettreAJourStatistiqueJoueur(self, joueur, stat):

        match stat:
            case "But":
                joueur.marquerUnBut()
            case "Passe":
                joueur.effectuerUnePasseDecisive()
            case "Carton jaune":
                joueur.recevoirUnCartonJaune()
            case "Carton rouge":
                joueur.recevoirUnCartonRouge()

joueur1 = Joueur("Doe", 15, "Defenseur")
joueur2 = Joueur("Dupont", 15, "Defenseur")
joueur3 = Joueur("Dupond", 15, "Defenseur")
joueur4 = Joueur("Jean", 15, "Defenseur")

equipe1 = Equipe("Olympique de Marseille")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

equipe1.mettreAJourStatistiqueJoueur(joueur1, "But")
equipe1.mettreAJourStatistiqueJoueur(joueur2, "Passe")

equipe1.afficherStatistiquesJoueurs()