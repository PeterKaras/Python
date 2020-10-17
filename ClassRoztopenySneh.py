class Check:
    def kontrola(self,maxi=0):
        for cislo in self.cisla:
            if cislo.isdigit():
                if int(cislo)> maxi:
                    maxi = int(cislo)
            else:
                return "Ne"
        if len(self.cisla) == self.pocet:
            return maxi
        else:
            return "Ne"
    
class Main(Check):
    def __init__(self,cisla,pocet):
        self.cisla = cisla
        self.pocet = pocet

    def hlavny_cyklus(self,maxi,zostatok=0,vysledok=0,prestup=0):
        cislo = maxi
        for i in range(maxi-1):
            for j in range(self.pocet):
                if int(self.cisla[j]) >= cislo:
                    if prestup == 0:
                        zostatok = j+1
                        prestup = 1
                    elif ((j+1)-zostatok)>1:
                        vysledok += j - zostatok
                        zostatok = j+1
                        prestup = 1
                    else:
                        prestup = 1
                        zostatok = j+1
                else:
                    pass
            zostatok = 0
            cislo -= 1
            prestup = 0
        return vysledok
                    
    def __str__(self):
        znak = self.kontrola()
        if znak != "Ne":
            return str(self.hlavny_cyklus(znak))
        else:
            return "Nezadali ste cislo/cisla!"

cyklus = input("zadajte poce cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>= 1:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet cisiel na zadavanie: ").strip()
        if pocet.isdigit() and len(pocet)>= 1:
            cisla = input("Zadajte cisla: ").split()
            if len(cisla)>=1:
                print(Main(cisla,int(pocet)))
            else:
                print("Nezadali ste cislo!")
        else:
            print("Nezadali ste cislo!")
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
