import random 
class Player:
    def __init__(self):
        self.peekovanie = ["A","B","C","D"]
        self.nabeh = []
        self.home = []
        self.players = []
        self.pocet_hracov = 0
        self.poradie_hracov = []

    def nacitanie_hracov(self):
        self.pocet_hracov = input("Zadajte pocet hracov (najviac 4 aspon 2): ").strip()
        if self.pocet_hracov.isdigit() and len(self.pocet_hracov)>=1 and int(self.pocet_hracov) < 5:
            self.peek_hracov()
            self.pocet_domov()
        else:
            return "Prepracovat"

    def peek_hracov(self,players=[]):
        for i in range(int(self.pocet_hracov)):
           hrac = random.choice(self.peekovanie)
           self.peekovanie.remove(str(hrac))
           players.append(hrac)
        self.poradie(players)

    def poradie(self,players):
        while True:
            for i in enumerate(players):
                if random.randint(1,6) == 6:
                    self.poradie_hracov.append(i[1])
                    players.remove(i[1])
                    print(self.poradie_hracov)
                if len(self.poradie_hracov) == int(self.pocet_hracov):
                    break
            if len(self.poradie_hracov) == int(self.pocet_hracov):
                    break
                
            
    def pocet_domov(self):
        if ((int(self.rozhranie)-3)//2) < 5:
            for i in range(int(self.pocet_hracov)):
                self.nabeh.append(list(self.poradie_hracov[i]*((int(self.rozhranie)-3)//2)))
                self.permission.append(["False" for x in range(((int(self.rozhranie)-3)//2))])
                self.kroky.append(["-1" for i in range((int(self.rozhranie)-3)//2)])
            print(self.nabeh)
        else:
            for i in range(int(self.pocet_hracov)):
                self.home.append(list(self.poradie_hracov[i]*4))
                self.permission.append(["False" for x in range(4)])
                self.kroky.append(["-1" for i in range(4)])

class Main(Player):
    def __init__(self):
        super().__init__()
        self.rozhranie = 0
        self.pocet_policok = 0
        self.permission = []
        self.kroky = []

    def rozmedzie_pola(self):
        self.rozhranie = input("Zadajte velkost hry v neparnych cislach(x>4): ").strip()
        if self.rozhranie.isdigit() and len(self.rozhranie) >= 1:
            if int(self.rozhranie) %2!=0:
                self.pocet_policok = (int(self.rozhranie)*4)-4
            else:
                return "Prepracovat"
        else:
            return "Prepracovat"

    def hlavny_cyklus(self,p=0):
        print("somn tu")
        while True:
            for letter in enumerate(self.poradie_hracov):
                indexy = letter[0]
                if "True" in self.permission[indexy]:
                    pass                        
                else:
                    if random.randint(1,6) == 6:
                        self.permission[indexy][0] = "True"
                        self.kroky[indexy][0] = 0
                        pass
                    else:
                        continue
                    
                hod = random.randint(1,6)    
                if hod == 6:
                    while True:
                        self.hod_sestky(indexy,hod)
                        hod = random.randint(1,6)
                        if hod != 6:
                            self.move(indexy,hod)
                            break
                        else:
                            self.hod_sestky(indexy,hod)
                else:
                    self.move(indexy,hod)
                    pass
            p += 1
            if p == 10:
                break
                    
    def move(self,indexy,hod,slovo=""):
        slovo = ""
        print(self.kroky)
        #print(self.permission)
        print(self.poradie_hracov)
        print(hod)
        for i in range(len(self.poradie_hracov[indexy])):
            kroky = self.kroky[indexy][i] + hod
            print("TOTOTOTOOTOTOPT",type(self.kroky[indexy][i]))
            if self.kroky[indexy][i] == "-1":
                continue
            elif kroky < int(self.pocet_policok):
                continue
            else:
                print("KROKY",kroky)
                if int(kroky) < int(self.pocet_policok):
                    print("SOM TU DO PICE MATERINEJ!")
                    slovo = "kick"
                else:
                    print("KOKOT BACOV")
               
        
        for i in range(len(self.poradie_hracov[indexy])):
            if self.kroky[indexy][i] == "-1":
                continue
            else:
                print(self.poradie_hracov[indexy][i])
                if int(self.kroky[indexy][i])+hod <= int(self.pocet_policok)-1:
                    self.kroky[indexy][i] = int(self.kroky[indexy][i])+hod
                else:
                    pass
                if int(self.kroky[indexy][i])>= int(self.pocet_policok)-1:
                    print("aha")
                    
        if slovo == "kick":
            print("kick")
            hod1 = random.randint(1,6)
            slovo = ""
            #self.move(indexy,hod1)
        #print("K",self.kroky)
               
    def hod_sestky(self,indexy,hod,vyber="12"):   
        if "False" in self.permission[indexy]:
            if random.choice(vyber) == "1": 
                for j in range(len(self.permission[indexy])):
                    if self.permission[indexy][j] == "False":
                        self.permission[indexy][j] = "True"
                        self.kroky[indexy][j] = 0
            else:
                self.move(indexy,hod)
        else:
            self.move(indexy,hod)
    
    def __str__(self):
        if self.rozmedzie_pola() != "Prepracovat":
            if self.nacitanie_hracov() != "Prepracovat":
                return str(self.hlavny_cyklus())
            else:
                return "Prepracovat"
        else:
            return "Prepracovat"

if __name__ == "__main__":
    print(Main())





