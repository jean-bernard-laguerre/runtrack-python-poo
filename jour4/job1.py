class Personne:
    def __init__(self):
        self.age = 14

    def modifierAge(self, age):
        self.age = age

    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello")
    

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours.")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    
class Professeur(Personne):
    def __init__(self, matiere):
        Personne.__init__(self)
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print(f"Le cours de {self.__matiereEnseignee} va commencer.")

etudiant = Eleve()

etudiant.afficherAge()
etudiant.bonjour()
etudiant.allerEnCours()
etudiant.modifierAge(15)

prof = Professeur("Mathematique")

prof.modifierAge(40)
prof.bonjour()
prof.enseigner()