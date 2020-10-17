pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla = []
cisla1 = ""
i = 0
j = 0
k = 0
zoradenie = []
hviezdy = ""
tvar = []
pocet = 0
index2= []
index = 0
vysledok = ""
zostatok = []
index3 = []
vysledok1 = 0
pocet1 = 0
prikaz = 0


while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet cisiel na zadavanie: "))
    cislo1 = input("Zadajte cisla: ")
    for cislo in str(cislo1):
        if cislo == " ":
            pass
        else:
            cisla.append(str(cislo))
            zoradenie.append(int(cislo))
            cisla1 += cislo
            
    #print(cisla)
    for i in range(len(zoradenie)-1,0,-1):
        for j in range(i):
            if zoradenie[j] < zoradenie[j+1]:
                temp = zoradenie[j]
                zoradenie[j] = zoradenie[j+1]
                zoradenie[j+1] = temp
                
    #print(zoradenie)
    pocet = zoradenie[0]
    
    hviezdy = "*" * pocet_cisiel
    for znak in hviezdy:
        tvar.append(znak)
    zostatok = tvar
    #print(tvar)
    i = zoradenie[0]
    j = 0
    
    for cislo in range(pocet):
        for cislo1 in cisla:
            #print("Som tu")
            if cisla[j] == str(i):
                #print("Som tu")
                index2.append(str(j))
            j += 1
            
        print("i",index2)
        
        dlzka = len(index2)
        for znak in range(dlzka):
            index = int(index2[k])
            #print(index)
            tvar[index] = "X"
            k += 1
            
        #print(tvar)
        for znak in tvar:
            vysledok += znak

        #print(vysledok)
        """if i == 1:
            print(cisla1)"""
        
        j = 0
        k = 0
        
        for znak in tvar:
            if tvar[j] == "X":
                #print("Som tu")
                index3.append(str(j))
            j += 1
            
        #print(index3)
        j = 0
        dlzka1 = len(index3)
        #print(dlzka1)
    
        if dlzka1 == 1:
            pass
        else:
            for znak in range(int(index3[-1])):
                if j < int(index3[0]):
                    j += 1
                    pass
                else:
                    for cislo in index3:
                        if j == int(cislo):
                            #print(j,int(cislo))
                            break
                        else:
                            #print(j,cislo)
                            pocet1 += 1
                    j += 1
        
                if pocet1 == dlzka1:
                    vysledok1 += 1
                
                pocet1 = 0
            
        #print(vysledok1)
        
        i -= 1
        j = 0
        k = 0
        index3 = []
        index2 = []
        tvar = []
        vysledok = ""
        tvar = zostatok
        pocet = 0
        

    print(vysledok1)
    cisla = []
    cisla1 = ""
    i = 0
    j = 0
    k = 0
    zoradenie = []
    hviezdy = ""
    tvar = []
    pocet = 0
    index2= []
    index = 0
    vysledok = ""
    zostatok = []
    index3 = []
    vysledok1 = 0
    pocet1 = 0
    prikaz = 0

    pocet_cyklov -= 1
