import sys
class Loading:
    def __init__(self):
        self.initial = None
        self.X_blocked = []
        self.Y_blocked = []

    def nacitanie(self):
        self.initial = input("Zadajte pocet prekazok a krokov: ").split()
        if len(self.initial)!= 2:
            return "Prepracovat"
        elif self.initial[0].isdigit() and self.initial[1].isdigit():
            for i in range(int(self.initial[0])):
                first_part = input("Zadajte suradnice prekazok: ").split()
                if len(first_part)==2 and first_part[0].replace("-","",1).isdigit() and \
                   first_part[1].replace("-","",1).isdigit():
                    self.X_blocked.append(first_part[0])
                    self.Y_blocked.append(first_part[1])
                else:
                    return "Prepracovat"
            self.alignment()
        else:
            return "Prepracovat"

    def alignment(self):
        for i in range(len(self.Y_blocked)-1,0,-1):
            for j in range(i):
                if int(self.Y_blocked[j]) > int(self.Y_blocked[j+1]):
                    temp = self.Y_blocked[j]
                    self.Y_blocked[j] = self.Y_blocked[j+1]
                    self.Y_blocked[j+1] = temp

                    temp = self.X_blocked[j]
                    self.X_blocked[j] = self.X_blocked[j+1]
                    self.X_blocked[j+1] = temp
        print(self.Y_blocked)
        print(self.X_blocked)

class Main(Loading):
    def __init__(self):
        super().__init__()
        
    def hlavny_cyklus(self,x_pos=0,y_pos=0,slovo="",maxi_u=sys.maxsize,maxi_d=sys.maxsize):
        #self.creating_pos()
        while int(self.initial[1])!=0:
            for badge in enumerate(self.X_blocked):
                if str(x_pos+1) == badge[1] and int(self.Y_blocked[badge[0]]) == y_pos:
                    slovo = "MoveOn"
                    break
                else:
                    slovo = "add"
            if slovo == "add":
                x_pos += 1
                self.initial[1] = int(self.initial[1])-1
                
            elif slovo =="MoveOn" and str(x_pos) not in self.X_blocked:
                mini_d,mini_u,y_pos,x_pos= self.finding_minimum(y_pos,x_pos,1)
                print("mini",mini_d,mini_u)
                
                for badge in enumerate(self.X_blocked):
                    if x_pos < int(badge[1]) and int(self.Y_blocked[badge[0]])==y_pos+(mini_u+1) and mini_u<=mini_d:
                        range_right = abs(int(badge[1])-x_pos)
                        if range_right < maxi_u:
                            maxi_u = range_right
                            
                    if x_pos < int(badge[1]) and int(self.Y_blocked[badge[0]])== y_pos-(mini_d+1) and mini_u>=mini_d:
                        print("som tu")
                        range_right = int(badge[1])-x_pos
                        if range_right < maxi_d:
                            maxi_d = range_right
                
                print("maxi222",maxi_d, maxi_u)            
                if maxi_u == sys.maxsize:
                    if y_pos+(mini_u+1) not in self.Y_blocked:
                        maxi_u = int(self.initial[1])
                    else:
                        maxi_u = 0

                if maxi_d == sys.maxsize:
                    if y_pos-(mini_d+1) not in self.Y_blocked:
                        maxi_d = int(self.initial[1])
                    else:
                        maxi_d = 0
                    
                print("maxi",maxi_d, maxi_u)
                if maxi_d <= maxi_u or maxi_d == sys.maxsize and maxi_u !=sys.maxsize:
                    y_pos += mini_u+1
                    self.initial[1] = int(self.initial[1])- (mini_u+1)
                else:
                    if maxi_d <= 0:
                        y_pos -= (abs(mini_d)+1)
                    else:
                        y_pos -= abs(mini_d+1)
                    self.initial[1] = int(self.initial[1])-abs(mini_d+1)
            else:
                mini_d,mini_u,y_pos,x_pos = self.finding_minimum(y_pos,x_pos,0)
                print(mini_d,mini_u)
                """for znak in enumerate(self.X_blocked):
                    if int(znak[1]) == x_pos:"""
                        
                self.initial[1] = int(self.initial[1])-1
            print("YX",y_pos,x_pos)
            
            if int(self.initial[1]) == 0:
                break
            maxi_u=sys.maxsize
            maxi_d=sys.maxsize
            slovo = ""
        return x_pos

    def finding_minimum(self,y_pos,x_pos,shifting,mini_d=sys.maxsize,mini_u=sys.maxsize):
        down = sys.maxsize
        up = sys.maxsize
        for badge in enumerate(self.X_blocked):
            if badge[1] == str(x_pos+shifting):
                if y_pos > int(self.Y_blocked[badge[0]]):
                    range_down = abs(y_pos-int(self.Y_blocked[badge[0]]))
                    if range_down < mini_d and abs(down)-abs(int(self.Y_blocked[badge[0]]))>=2:
                        #print("TTUTUTU",range_down)
                        mini_d = range_down
                    down = int(self.Y_blocked[badge[0]])
                elif y_pos == int(self.Y_blocked[badge[0]]):
                    spare = 0
                else:
                    range_up = (int(self.Y_blocked[badge[0]])-y_pos)
                    #print("halo",int(self.Y_blocked[badge[0]]),up)
                    if range_up < mini_u and (abs(abs(int(self.Y_blocked[badge[0]]))-abs(up))<=1 or up == sys.maxsize):
                        #print(range_up,abs(int(self.Y_blocked[badge[0]])-up))
                        mini_u = range_up
                    up = int(self.Y_blocked[badge[0]])
      
        if mini_u == sys.maxsize:
            mini_u = spare
        elif mini_d == sys.maxsize:
            mini_d = spare 
        return mini_d,mini_u,y_pos,x_pos
        
    def __str__(self):
        if self.nacitanie() != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return "Prepracovat"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>=1:
    while int(cyklus)!=0:
        print(Main())
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
