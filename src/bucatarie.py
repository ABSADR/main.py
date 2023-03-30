import json


class Bucatarie:
    def __init__(self):
        with open("Inventar.json") as f:
            self.inventar = json.load(f)

    def adauga_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar:
            self.inventar[nume_produs] += cantitate
        else:
            self.inventar[nume_produs] = cantitate

        with open("Inventar.json", "w") as f:
            json.dump(self.inventar, f)

    def scadere_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar:
            if self.inventar[nume_produs] >= cantitate:
                self.inventar[nume_produs] -= cantitate
            else:
                print("Nu exista suficient {} in inventar.".format(nume_produs))
        else:
            print("Ingredientul {} nu exista in inventar.".format(nume_produs))



bucatarie= Bucatarie()
bucatarie.adauga_produs('oua',6)
bucatarie.scadere_produs('lapte', 55)



with open('Inventar.json', 'r') as file:
    d = json.load(file)
    print(d)

