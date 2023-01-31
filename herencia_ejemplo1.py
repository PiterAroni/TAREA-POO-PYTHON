class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo",type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
    def describeme(self):
        print("Soy un Animal del tipo",type(self).__name__)

class Vaca(Animal):
    def hablar(self):
        print("Muuuu!")
    def describeme(self):
        print("Soy un Animal del tipo",type(self).__name__)

#INSTANCIAR
mi_perro = Perro("mamifero",10)
mi_vaca = Vaca("mamifero",23)
mi_perro.describeme()
mi_perro.hablar()
mi_vaca.describeme()
mi_vaca.hablar()
