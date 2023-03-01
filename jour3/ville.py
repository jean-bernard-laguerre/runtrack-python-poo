class Ville:
    def __init__(self, nom, pop):
        self.__nom = nom
        self.__population = pop

    def getPopulation(self):
        return self.__population
    
    def getNom(self):
        return self.__nom
    
    def setPopulation(self, pop):
        self.__population = pop
    
class Personne:
    def __init__(self, nom, age, ville) -> None:
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation(ville)
    
    def ajouterPopulation(self, ville):
        ville.setPopulation(ville.getPopulation() + 1)

paris = Ville("Paris", 1000000)
print(f"{paris.getNom()}: {paris.getPopulation()}")

marseille = Ville("Marseille", 861635)
print(f"{marseille.getNom()}: {marseille.getPopulation()}")

perso1 = Personne("John", 45, paris)
perso2 = Personne("Myrtille", 4, paris)
perso3 = Personne("Chloé", 18, marseille)

print(f"{paris.getNom()}: {paris.getPopulation()}")
print(f"{marseille.getNom()}: {marseille.getPopulation()}")