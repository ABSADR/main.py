
from bucatarie import *


class Reteta:
    def __init__(self,nume,ingrediente):
        self.nume = nume
        self.ingrediente = ingrediente

    def pregatire(self, bucatarie):
        for ingredient, cantitate in self.ingrediente.items():
            bucatarie.scazut_produs(ingredient['nume'], ingredient['cantitate'])
bucatarie=Bucatarie()
reteta= Reteta('Clatite' , 'lapte')
bucatarie.scadere_produs('lapte' , 400)

with open('inventar.json', 'r') as file:
    d = json.load(file)
    print(d)