class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def viellir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

animal1 = Animal()
print(f"L'animal a {animal1.age} an(s)")
animal1.viellir()
print(f"L'animal a {animal1.age} an(s)")
animal1.nommer("Luna")
print(f"L'animal se nomme {animal1.prenom}")
