class Infectado_especial_L4D2:
    def atacar(self):
        pass

class Hunter(Infectado_especial_L4D2):
    def atacar(self):
        print("Rasguñar")

class Charger(Infectado_especial_L4D2):
    def atacar(self):
        print("Embestir")

for Infectado_especial_L4D2 in Hunter(), Charger():
    Infectado_especial_L4D2.atacar()