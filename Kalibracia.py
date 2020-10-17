class Check:
    #Checkuje ci sa tam nenachadza nieco neziaduce
    def kontrola(self,znaky):
        for pismeno in znaky:
            if pismeno.upper() == "B" or pismeno.upper() == "C" or pismeno == "?":
                pass
            else:
                return "Prepracovat"
   
        if len(znaky) != int(self.sirka):
            return "Prepracovat"
             
    def nacitanie(self):
        for i in range(int(self.dlzka)):
            riadok = input("Zadajte vase prikazy: ").strip()
            if self.kontrola(riadok) != "Prepracovat":
                self.pole.append(list(riadok))
            else:
                return "Prepracovat"
    
class Line:
    #Prechadza po riadku cisla a kontrolu
    def prechadzanie_line(self,zostatok=""):
        for i in range(self.dlzka):
            for j in range(self.sirka):
                if self.pole[i][j] == "B" and zostatok == "C":
                    pass
                elif self.pole[i][j] == "?" and zostatok == "B":
                    self.pole[i][j] = "C"
                elif self.pole[i][j] == "?" and zostatok == "C":
                    self.pole[i][j] = "B"
                elif self.pole[i][j] == zostatok:
                    return "Skuste znovu"
                elif self.pole[i][j] == "?" and zostatok == "":
                    continue
                else:
                    zostatok = self.pole[i][j]
                zostatok = self.pole[i][j]
            zostatok = ""
        return "ok"

class Low:
    #Prechadza po stlpci a kontroluje
    def prechadzanie_verticle(self,zostatok=""):
        for i in range(self.sirka):
            for j in range(self.dlzka):
                if self.pole[j][i] == "B" and zostatok == "C":
                    pass
                elif self.pole[j][i] == "?" and zostatok == "B":
                    self.pole[j][i] = "C"
                elif self.pole[j][i] == "?" and zostatok == "C":
                    self.pole[j][i] = "B"
                elif self.pole[j][i] == zostatok:
                    return "Skuste znovu"
                elif self.pole[j][i] == "?" and zostatok == "":
                    continue
                else:
                    zostatok = self.pole[j][i]
                zostatok = self.pole[i][j]
            zostatok = ""
        return "Kalibracia prebehla uspesne"
            
class Main(Check,Line,Low):
    #Main cyklus 
    def __init__(self,rozmedzie):
        self.dlzka = int(rozmedzie[0])
        self.sirka = int(rozmedzie[1])
        self.pole = []

    def __str__(self):
        if self.nacitanie() != "Prepracovat":
            if self.prechadzanie_line() == "ok":
                return str(self.prechadzanie_verticle())
            else:
                return "Skuste znovu"
        else:
            return "Nezadali ste pozadovane znaky!"

cyklus = input("zadajte pocet cyklov: ").strip()
if cyklus.isdigit():
    while int(cyklus) != 0:
        rozmedzie = input("Zadajte rozmedzie pola: ").split()
        if len(rozmedzie) == 2:
            if rozmedzie[0].isdigit() and rozmedzie[1].isdigit():
                print(Main(rozmedzie))
            else:
                print("Nezadali ste cislo!")
        else:
            print("Nezadali ste 2 znaky!")
            continue
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo!")
