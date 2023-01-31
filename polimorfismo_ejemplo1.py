class Animal_de_granja:
    def hablar(self):
        pass

class Gallo(Animal_de_granja):
    def hablar(self):
        print("Quiquiriki!!!")

class Cerdo(Animal_de_granja):
    def hablar(self):
        print("Oink!!")

for animal_de_granja in Gallo(), Cerdo():
    animal_de_granja.hablar()