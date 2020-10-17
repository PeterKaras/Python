import random
class Player:
    def __init__(self):
        self.interface = None
        self.maxi_steps = None
        self.foot_tile = None
        self.num_homes = None
        self.players = []

    def loading(self):
        num_players = input("Zadajte pocet hracov: ").strip()
        if len(num_players)>= 1 and num_players.isdigit() and 0 < int(num_players) <= 4:
            self.interface = input("Zadajte dlzku pola (x>=5 a x<=11 - neparne): ").strip() 
            if len(self.interface)>= 1 and self.interface.isdigit() and 5 <= int(self.interface) <= 11:
                self.maxi_steps = (int(self.interface)-1)*4 #generate maxi steps in environment
                self.foot_tile = [[] for column in range(int(self.interface))] #generate the indexes of each tile
                print(self.foot_tile)
                self.solving_homes(num_players)
            else:
                print("Wrong input!")
        else:
            print("Wrong input!")

    #Computing the number of homes 
    def solving_homes(self,num_players):
        self.num_homes = (int(self.interface)//2)-1
        self.goin_players(num_players)

    #Stating the essential parameters
    def goin_players(self,num_players):
        self.permission = [[False for column in range(int(self.num_homes))]  
                    for row in range(int(num_players))] #stating False value to unabandoned figures
        self.path = [["-1" for column in range(int(self.num_homes))]  
                    for row in range(int(num_players))] #computing the steps which were made by each figures
        self.cross = [["o" for column in range(int(self.num_homes))]  
                    for row in range(int(num_players))] #stating if the figure cross the initial point
        self.choosing_players(num_players)

    def choosing_players(self,num_players,peeking=["A","B","C","D"]):
        player_to_pick = []
        for i in range(4-int(num_players)):
            peeking.remove(random.choice(peeking))
        self.layout_player(num_players,peeking)
    
    #random sequal of figures
    def layout_player(self,num_players,player_to_pick):
        while True:
            for i in enumerate(player_to_pick):
                if random.randint(1,6) == 6:
                    self.players.append(i[1])
                    player_to_pick.remove(i[1])
                if len(self.players) == int(num_players):
                    return 0
                
class Environment(Player):
    def __init__(self):
        self.field = []
        self.range_field = None
        self.help_field = self.field 

    def creating_field(self):
        self.range_field = int(self.interface)//2
        self.field.append(list("***"))
        self.semi_points()
        self.next_to_mid()
        self.mid_points()
        self.next_to_mid()
        self.semi_points()
        self.field.append(list("***"))

    def semi_points(self):
        for i in range(self.range_field-2):
            self.field.append(list("*O*"))

    def next_to_mid(self):
        string = "*"*self.range_field+"O"+"*"*self.range_field
        self.field.append(list(string))

    def mid_points(self):
        string = mid = "*"+"O"*(self.range_field-1)+" "+"O"*(self.range_field-1)+"*"
        self.field.append(list(string))

    def creating_paths(self):
        shift = self.range_field-1
        steps = 1
        word = "down"
        while steps <= (int(self.interface)-1)*4:
            for i in range(len(self.field[shift])):
                if self.field[shift][i] == "O" or 0 > i < int(self.interface):
                    break
                else:
                    if shift >= self.range_field:
                        self.foot_tile[shift].insert(0,steps)
                    else:
                        self.foot_tile[shift].append(steps)
                steps += 1
                if steps > (int(self.interface)-1)*4:
                    break

            if word == "down":
                shift -= 1
            elif word == "up":
                shift += 1
                
            if shift >= int(self.interface):
                word = "down"
                shift -= 2
                
            if shift == -1:
                shift += 2
                word = "up"

    def displaying_field(self):
        for i in range(len(self.field)):
           print("{:^60}".format("".join(self.field[i])))
        print()
    
class Main(Environment,Player):
    def __init__(self):
        Player.__init__(self)
        Environment.__init__(self)
        self.home = []
    
    def main_loop(self):
        self.creating_field()
        self.creating_paths()
        counter = 0
        while True:
            for znak in enumerate(self.players):
                #if There is True value in self.permission so he can move and doesnt have to wait till 6
                if True in self.permission[znak[0]]:
                    znak = self.next_step(znak)
                    if znak != None:
                        return znak
                else:
                    num_dice = random.randint(1,6)
                    if num_dice == 6:
                        self.moving_in(znak)

    def next_step(self,znak):
        num_dice = random.randint(1,6)
        if num_dice == 6:
            while True:
                self.num_six(znak,num_dice)
                num_dice = random.randint(1,6)
                if num_dice != 6:
                    self.move(znak,num_dice)
                    break
        else:
            self.move(znak,num_dice)
            
        if self.num_homes == self.permission[znak[0]].count("END"):
            return str(znak[1])
            

    #Setting up the positions of each figures
    def moving_in(self,znak):
        position_false = self.permission[znak[0]].index(False)
        self.permission[znak[0]][position_false] = True
        if znak[1] == "A":
            self.field[self.range_field-1][0] = "A"
            self.path[znak[0]][position_false] = self.foot_tile[self.range_field-1][0]
        elif znak[1] == "B":
            self.field[0][2] = "B"
            self.path[znak[0]][position_false] = self.foot_tile[0][2]
        elif znak[1] == "C":
            self.field[self.range_field+1][-1] = "C"
            self.path[znak[0]][position_false] = self.foot_tile[self.range_field+1][-1]
        else:
            self.field[-1][0] = "D"
            self.path[znak[0]][position_false] = self.foot_tile[-1][0]

    def num_six(self,znak,num_dice):
        if False in self.permission[znak[0]]:
            if random.choice("12") == "1":
                self.moving_in(znak)
                return 0
        self.move(znak,num_dice)

    def move(self,znak,hod):
        slovo=""
        for i in range(len(self.permission[znak[0]])):
            if (znak[1] == "A" and int(self.path[znak[0]][i])+hod > self.maxi_steps) or self.path[znak[0]][i] == "-1" or \
               (int(self.path[znak[0]][i])+hod > (int(self.interface)-1)*(ord(znak[1])-ord("A")) and self.cross[znak[0]][i] == "n"):
                continue
            else:
                for j in range(len(self.path)):
                    if j == znak[0]:
                        pass
                    else:
                        for k in range(len(self.permission[j])):
                            if self.path[j][k] == "-1":
                                continue
                            else:
                                if int(self.path[j][k]) == 1 or int(self.path[j][k]) == int(self.interface) or int(self.path[j][k]) == (int(self.interface)*2)-1 or\
                                   int(self.path[j][k]) == (int(self.interface)*3)-2:
                                    continue
                                else:
                                    if int(self.path[znak[0]][i])+hod == int(self.path[j][k]):
                                        self.path[j][k] = "-1"
                                        self.cross[j][k] = "o"
                                        self.counting_steps(znak,hod)
                                        self.permission[j][k] = False
                                        slovo = "kick"                                       
            if slovo == "kick":
                self.move(znak,random.randint(1,6))
        self.counting_steps(znak,hod)

    def counting_steps(self,znak,hod):
        for i in range(len(self.permission[znak[0]])):
            if self.path[znak[0]][i] == "-1":
                continue
            else:
                if znak[1] == "A":
                    if int(self.path[znak[0]][i])+hod < int(self.maxi_steps):
                        self.path[znak[0]][i] = int(self.path[znak[0]][i])+hod
                        break
                    elif int(self.maxi_steps) < int(self.path[znak[0]][i])+hod  <= self.num_homes+int(self.maxi_steps):
                        if int(self.path[znak[0]][i])+hod not in self.home:
                            self.home.append((int(self.path[znak[0]][i])+hod))
                            self.path[znak[0]][i] = "-1"
                            self.permission[znak[0]][i] = "END"
                            break
                        else:
                            continue
                    else:
                        pass
                else:
                    if self.checking(znak[0],i,ord(znak[1])-ord("A"),hod) == "pridal":
                        break
        self.import_path(znak)

    def checking(self,indexy,i,nasobenie,hod):
        if int(self.path[indexy][i])+hod > int(self.maxi_steps) and self.cross[indexy][i] == "o":
            self.path[indexy][i] = (int(self.path[indexy][i])+hod)-(int(self.maxi_steps))
            self.cross[indexy][i] = "n"
            return "pridal"
        elif (int(self.interface)*nasobenie)-nasobenie < int(self.path[indexy][i])+hod <= ((int(self.interface)*nasobenie)-nasobenie)+self.num_homes \
             and self.cross[indexy][i] == "n":
            if int(self.path[indexy][i])+hod not in self.home:
                self.home.append((int(self.path[indexy][i])+hod))
                self.path[indexy][i] = "-1"
                self.permission[indexy][i] = "END"
                return "pridal"
            else:
                return "nepridal"
        elif int(self.path[indexy][i])+hod > ((int(self.interface)*nasobenie)-nasobenie) and self.cross[indexy][i] == "n":
            return "nepridal"
        else:
            self.path[indexy][i] = int(self.path[indexy][i])+hod
            return "pridal"

    def import_path(self,znak):
        for i in range(len(self.path)):
            for j in range(len(self.path[i])):
                if self.path[i][j] == "-1":
                    continue
                else:
                    for k in range(len(self.foot_tile)):
                        if self.path[i][j] in self.foot_tile[k]:
                            position = self.foot_tile[k].index(self.path[i][j])
                            self.appending_to_field(k,position,znak,self.path[i][j],i)
                            break
        self.appending_homes()
        self.displaying_field()
        self.field = []
        self.creating_field()

    def appending_to_field(self,k,position,znak,number,i):
        counter = 0
        computer = 0
        for letter in self.field[k]:
            if letter == "O" or letter == " ":
                computer += 1 
            else:
                if counter == position and number not in self.home:
                    self.field[k][counter+computer] = self.players[i]
                counter += 1

    def appending_homes(self):
        for i in range(len(self.home)):
            if int(self.maxi_steps) < int(self.home[i]) <= int(self.maxi_steps)+self.num_homes:
                pozicia = int(self.home[i])-int(self.maxi_steps)
                self.field[self.range_field][pozicia] = "A"
            elif self.foot_tile[self.range_field][-1] < int(self.home[i]) <= self.foot_tile[self.range_field][-1]+self.num_homes:
                pozicia =( self.range_field)+(int(self.home[i])-self.foot_tile[self.range_field][-1])
                self.field[self.range_field][pozicia] = "C"
            elif self.foot_tile[0][1] < int(self.home[i]) <= self.foot_tile[0][1]+self.num_homes:
                if int(self.home[i]) == self.foot_tile[0][1]+self.num_homes:
                    self.field[self.range_field-1][self.range_field] = "B"
                else:
                    pozicia = (int(self.home[i])-self.foot_tile[0][1])
                    self.field[pozicia][1] = "B"     
            elif self.foot_tile[-1][1] < int(self.home[i]) <= self.foot_tile[-1][1]+self.num_homes:
                if int(self.home[i]) == self.foot_tile[-1][1]+self.num_homes:
                    self.field[self.range_field+1][self.range_field] = "D"
                else:
                    pozicia = (int(self.home[i])-self.foot_tile[-1][1])+self.range_field
                    self.field[pozicia+1][1] = "D"
                
    def __str__(self):
        self.loading()
        return self.main_loop()

if __name__ == "__main__":
    print(Main(),"won!")






























    
