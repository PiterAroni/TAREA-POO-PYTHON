class Gato(object):
    def __init__(self,nombre,color,edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad
    
    def comer(self):
        print("El gato come pescado")

    def dormir(self):
        print("El gato duerme en el sofa")

#INSTANCIAR
gato1 = Gato("Mishifu","mostaza","2")
print(gato1.nombre)
print(gato1.color)
print(gato1.edad)
print(gato1.comer())
print(gato1.dormir())