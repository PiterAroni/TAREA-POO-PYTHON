class Personaje(object):
    def __init__(self,nombre,habilidad,nivel):
        self.nombre = nombre
        self.habilidad = habilidad
        self.nivel = nivel

    def atacar(self):
        print("El personaje atacó utilizando su habilidad")
    
    def comer(self):
        print("El personaje comió su comida favorita")

#INSTANCIAR
personaje1 = Personaje("Luffy","estirarse",50)
print(personaje1.nombre)
print(personaje1.habilidad)
print(personaje1.nivel)
print(personaje1.atacar())
print(personaje1.comer())

