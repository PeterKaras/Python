from itertools import product
class Loading:
    def nacitanie(self):
        for i in range(2):
            if i == 0:
                cisla = input("Zadajte rozmedzie pola: ").split()
                if cisla[0].isdigit() and cisla[1].isdigit():
                    self.sirka = int(cisla[0])
                    self.dlzka = int(cisla[1])
                    pass
                else:
                    return "Prepracovat"
            else:
                cisla = input("Zadajte pocet slov na zaciarkanie: ").split()
                if cisla[0].isdigit():
                    pass
                else:
                    return "Prepracovat"

            for j in range(self.sirka):
                slovo = input("Zadajte slovo: ").strip()
                if slovo.isalpha():
                    if i == 0 and len(slovo) == self.dlzka:
                        self.field.append(list(slovo))
                    elif i == 1:
                        self.hlavny_cyklus(slovo)
                    else:
                        return "Prepracovat"
    
class Main(Loading):
    def __init__(self):
        self.field = []
        self.sirka = 0
        self.dlzka = 0
        self.ik_1 = []
        self.jk_1 = []
        self.vysledok = ""

    def hlavny_cyklus(self,slovo,ik="",jk=""):
        for pismeno in slovo:
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    if self.field[i][j] == pismeno:
                        ik += str(i)
                        jk += str(j)
                    else:
                        continue
            self.ik_1.append(list(ik))
            self.jk_1.append(list(jk))
            ik = ""
            jk = ""
        print(self.ik_1)
        print(self.jk_1)
        self.horizontalne()
        self.ik_1 = []
        self.jk_1 = []
    
    def horizontalne(self):
        for cislo in product(*self.ik_1):
            zostatok = cislo[0]
            for i in range(len(cislo)):
                print(i)
                predosle = cislo[i]
                if i == len(cislo)-1:
                    self.odstranovanie(cislo)
                if int(zostatok) == int(predosle):
                    pass
                else:
                    break
                zostatok = cislo[i]
    def odstranovanie(self,cislo):
        print(cislo)
    
    def __str__(self):
        znak = self.nacitanie()
        if znak == "Prepracovat":
            return znak
        return str(self.vysledok)

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit():
    while int(cyklus)!=0:
        print(Main())
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
