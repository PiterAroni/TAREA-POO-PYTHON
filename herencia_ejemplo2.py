class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def acelerar(self):
        pass

    def arrancar(self):
        print(type(self).__name__,"que arrancó con n ruedas")

class Moto(Vehiculo):
    def acelerar(self):
        print("Aceleracion: 150km/h")
    def arrancar(self):
        print(type(self).__name__,"que arrancó con 2 ruedas")

class Carro(Vehiculo):
    def acelerar(self):
        print("Aceleracion 125km/h")
    def arrancar(self):
        print(type(self).__name__,"que arrancó con 4 ruedas")

#INSTANCIAR
mi_moto = Moto("rojo",2)
mi_carro = Carro("azul",4)
mi_moto.arrancar()
mi_moto.acelerar()
mi_carro.arrancar()
mi_carro.acelerar()