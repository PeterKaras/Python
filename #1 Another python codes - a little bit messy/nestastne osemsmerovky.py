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
                        self.guess.append(slovo)
                    else:
                        return "Prepracovat"
        
        
class Main(Loading):
    def __init__(self):
        self.sirka = 0
        self.dlzka = 0
        self.field = []
        self.guess = []
        self.indexy = []
    
    def hlavny_cyklus(self,word="",vysledok=""):
        for pocet in range(len(self.guess)):
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    if self.field[i][j] == self.guess[pocet][0]:
                        p = list(str(i)+str(j))
                        self.indexy.append(p)
            print(self.indexy)
            self.horizontalne(len(self.guess[pocet]))
            self.indexy = []

    def horizontalne(self,pocet,k=0,word=""):
        for i in range(len(self.indexy)):
            zaciatok = int(self.indexy[k][k])
            for j in range(len(self.field[zaciatok])):
                if j >= zaciatok-pocet+1:
                    word += self.field[zaciatok][j]
                if word[::-1] in self.guess or word in self.guess:
                    for k in range(len(self.field[i])):
                        if self.field[i][k] == word[j]:
                            self.field[i][k]= " "
                            j += 1
                        if j == len(word):
                            break
                    print(self.field)
                    return 0
                if j == int(self.indexy[k][k+1]):
                    word = ""
                    word += self.field[zaciatok][j]
            k += 2
        return self.vertikalne(pocet)
    
    def vertikalne(self,pocet,k=0,word=""):
        print(self.indexy[k])
        for i in range(len(self.indexy)):
            zaciatok = int(self.indexy[k][k+1])
            for j in range(self.sirka):
                if j >= zaciatok-pocet+1:
                    word += self.field[j][zaciatok]
                    print(word)
                if word[::-1] in self.guess or word in self.guess:
                    print(word)
                    for k in range(len(self.field[i])):
                        if self.field[i][k] == word[j]:
                            self.field[i][k]= " "
                            j += 1
                            if j == len(word):
                                break
                    print(self.field)
                    return 0
                if j == int(self.indexy[k][k+1]):
                    word = ""
                    word += self.field[j][zaciatok]
            k += 2
        return self.diagonal(pocet)
    
    def diagonal(self,k=0):
        p = int(self.indexy[k][k])
        zaciatok = int(self.indexy[k][k+1])
        for i in range(self.dlzka):
            if p == self.sirka or p == self.dlzka:
                continue
            else:
                print(self.field[p][zaciatok])
                zaciatok += 1
                p += 1
        
    def __str__(self):
        znak = self.nacitanie()
        if znak != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return znak
            
cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit():
    while int(cyklus)!=0:
        print(Main())
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")    
