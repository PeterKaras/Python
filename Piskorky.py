class Main:
    def __init__(self):
        self.field = [[1,2,3],[4,5,6],[7,8,9]]
        
    def hlavny_cyklus(self,i=0,rounds = 0):
        while True:
            if i == 0:
                player = input("(1) Zadajte vasu poziciu: ").strip()
                if player.isdigit() and len(player)>=1:
                    znak = "X"
                    labelling = 1
                    i += 1
                else:
                    continue
            else:
                player = input("(2) Zadajte vasu poziciu: ").strip()
                if player.isdigit() and len(player)>=1:
                    znak = "O"
                    labelling = 2
                    i = 0
                else:
                    continue
                
            for j in range(3):
                if int(player) in self.field[j]:
                    self.field[j][self.field[j].index(int(player))] = znak
            self.displaying_env()
            
            if rounds >= 4:
                if self.checking(znak) == "win":
                    return str(labelling)+" has won the Game! Enemy is FOOL!" 
  
            rounds += 1
            if rounds == 9:
                return "DRAW!"      

    def checking(self,znak,first_dia=0,third_dia=0,third_ver=0,second_ver=0):
        for i in range(len(self.field)):
            #Kontrola stlpca prveho a zaroven riadky
            if str(self.field[i][0]) == znak:
                if self.field[i][0].count(znak) == 3:
                    return "win"
                
            #Dia z lava
            for j in range(3):
                if str(self.field[j][j]) == znak:
                    first_dia += 1
                    if first_dia == 3:
                        return "win"
            first_dia = 0
                        
        #Kontrola stlca druheho
        if str(self.field[0][1]) == znak:
            for j in range(3):
                if str(self.field[j][1]) == znak:
                    second_ver += 1
                    if second_ver == 3:
                        return "win"
                    
        #Kontrola stlca tretieho
        i = 2
        if str(self.field[0][2]) == znak:
            for j in range(3):
                if str(self.field[j][2]) == znak:
                    third_ver += 1
                    if third_ver == 3:
                        return "win"
                #Dia z prava
                if str(self.field[j][i]) == znak:
                    third_dia += 1
                    if third_dia == 3:
                        return "win"
                    i -= 1
                        
    def displaying_env(self):
        print()
        print("{:-^13}".format("-"))
        print("| " + str(self.field[0][0]) + " | " + str(self.field[0][1]) + " | " + str(self.field[0][2]) + " | ")
        print("{:-^13}".format(""))
        print("| " + str(self.field[1][0]) + " | " + str(self.field[1][1]) + " | " + str(self.field[1][2]) + " | ")
        print("{:-^13}".format(""))
        print("| " + str(self.field[2][0]) + " | " + str(self.field[2][1]) + " | " + str(self.field[2][2]) + " | ")
        print("{:-^13}".format(""))
        print()          
    
    def __str__(self):
        return self.hlavny_cyklus()

if __name__== "__main__":
    print(Main())
