import math
class check:
    def kontrola(self,cisla,pocet1,dopocet=0):
        for cislo in cisla:
            if cislo.isdigit():
                pass
            elif cislo.replace("-","",1).isdigit():
                pass
            else:
                return "Ne"
            dopocet += 1
        if dopocet == pocet1:
            return "ok"
        else:
            return "Ne"

class beggining(check):
    def nacitanie(self,cisla=[],pocetnost=2):
        for i in range(self.pocet):
            pole = input("Zadajte cisla: ").split()
            znak = self.kontrola(pole,pocetnost)
            if znak == "ok":
                cisla.append(pole)
            else:
                return "Ne"
        return cisla
    
class main(beggining):
    def __init__(self,pocet):
        self.pocet = pocet

    def hlavny_cyklus(self,pole,pocetnost=0):
        for i in range(len(pole)):
            for j in range(i+1,len(pole)):
                pocetnost += self.uhly(pole[i],pole[j])
        if pocetnost == 0:
            return "0.000000"
        else:
            pravdepodobnost = round(2/pocetnost,7)
            return pravdepodobnost

    def uhly(self,i,j):
        x = int(j[0]) - int(i[0])
        y = int(j[1]) - int(i[1])
        tangens = math.degrees(math.atan2(y, x))
        if tangens == 45:
            return 1
        else:
            return 0
        
    def __str__(self):
        pole = self.nacitanie()
        if pole != "Ne":
            pravde = str(self.hlavny_cyklus(pole))
        else:
            return "Nezadali ste cislo/cisla!"
        return str(pravde)

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit():
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet cisiel na zadavanie: ").strip()
        if pocet.isdigit():
            pole = main(int(pocet))
            print(pole)
            if pole == "Nezadali ste cisla!":
                print("weqewq")
                continue
            else:
                pass
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo!")
    
