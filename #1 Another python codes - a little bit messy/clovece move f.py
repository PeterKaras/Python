import random
pole = [['D', 'D'], ['C', 'C'], ['A','A']]
kroky = [[1, '0'], [17, '-1'], [0, '0']]
slovo = ""
hod = 2
rozhranie = 7
indexy = 1
koniec = 0
def move(indexy,hod,rozhranie,pole,kroky,slovo=""):
    
    for i in range(len(pole[indexy])):
        print(pole[indexy])
        if kroky[indexy][i] == "-1" or int(kroky[indexy][i])+hod >= 23:
            print("ok")
            continue
        else:
            print(pole[indexy][i])
            for j in range(len(pole)):
                if j == indexy:
                    continue
                else:
                    for k in range(len(pole[j])):
                        if kroky[j][k] == "-1":
                            continue
                        else:
                            
        
            
move(indexy,hod,rozhranie,pole,kroky)
for i in range(len(pole[indexy])):
    print(i)
    if pole[indexy][i] == "-1":
        pass
    else:

         """if abs(ord(self.poradie_hracov[indexy][i])-ord(self.poradie_hracov[j][k])) == 1:
                                    #jedno polovy rozdiel
                                    if int(self.kroky[j][k]) > int(self.kroky[indexy][i]):
                                        if int(self.kroky[j][k])-(int(self.rozhranie)-1) == int(self.kroky[indexy][i])+hod \
                                           and int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"
                                    else:  
                                        if int(self.kroky[indexy][i])-((int(self.rozhranie)-1)*3)+hod == int(self.kroky[j][k]) \
                                           and int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"
                                            
                                elif abs(ord(self.poradie_hracov[indexy][i])-ord(self.poradie_hracov[j][k])) == 2:
                                    #dvojpolovy rozdiel
                                    if int(self.kroky[j][k]) > int(self.kroky[indexy][i]):
                                        if int(int(self.kroky[j][k]))-((int(self.rozhranie)-1)*2) == int(self.kroky[indexy][i])+hod and \
                                            int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"
                                    else:
                                        if int(self.kroky[indexy][i])-((int(self.rozhranie)-1)*2)+hod == int(self.kroky[j][k]) and \
                                            int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"
                                else:
                                    #trojpolovy rozdiel
                                    if int(self.kroky[j][k]) < int(self.kroky[indexy][i]):
                                        if int(int(self.kroky[indexy][i]))-((int(self.rozhranie)-1)*1)+hod == int(self.kroky[j][k]) and \
                                            int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"
                                    else:
                                        if int(self.kroky[j][k])-((int(self.rozhranie)-1)*3) == int(self.kroky[indexy][i])+hod and \
                                            int(self.kroky[j][k]) != 0:
                                            slovo = "kick"
                                            self.permission[j][k] = "False"
                                            self.kroky[j][k] = "-1"""
        

        
                 
                
                                      
