class Student:
    def __init__(self, nom, prenom, num):
        self.__nom = nom
        self.__prenom = prenom
        self.__num = num
        self.__credit = 0
        self.__level = self.__studentEval()

    def addCredit(self, nbrCredit):

        if nbrCredit > 0:
            self.__credit += nbrCredit
            self.__level = self.__studentEval()

    def getCredit(self):
        print(f"Le nombre de credit de {self.__prenom} {self.__nom} est de {self.__credit} points")

    def __studentEval(self):
        if  90 <= self.__credit:
            return "Excellent"
        elif 80 <= self.__credit:
            return "Très Bien"
        elif 70 <= self.__credit:
            return "Bien"
        elif 60 <= self.__credit:
            return "Passable"
        else:
            return "Insuffisant"
        
    def info(self):
        print(f"Prenom: {self.__prenom}")
        print(f"Nom: {self.__nom}")
        print(f"Credit: {self.__credit}")
        print(f"Niveau: {self.__level}")


etudiant = Student("Doe", "John", "1866565")

etudiant.addCredit(40)
etudiant.addCredit(19)
etudiant.addCredit(17)

etudiant.info()