pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla = []
stred = 0
zvysok = 0
dlzka = 0
zostatok = []
zmena = 0
j = 0
i = 0
pocet = 0
vysledok = ""


while pocet_cyklov != 0:
    cisla = []
    stred = 0
    zvysok = 0
    dlzka = 0
    zostatok = []
    zmena = 0
    vysledok = ""
    j = 0
    i = 0
    pocet = 0
    
    cislo = input("Zadajte cislo :")
    for cislo1 in str(cislo):
        cisla.append(cislo1)
        zostatok.append(cislo1)
        if cislo1 == "9":
            #print("buh")
            pocet += 1
        
    #print(cisla)
    
    dlzka = len(cisla)
    
    if dlzka != 0:
        zvysok = dlzka % 2
        
        if zvysok != 0:
            stred = (dlzka//2)
            print(cisla[stred],stred)
            j = stred + 1
            i = stred - 1
            if cisla[stred] == "9":
                zmena = 9
                cisla[stred+1] = str(zmena)
                j += 1
                i -= 1
            else:
                zmena = int(cisla[stred]) + 1
                cisla[stred] = str(zmena)
                
            for cislo1 in cisla:
                if dlzka == pocet:
                    break
                if j == dlzka:
                    break
                cisla[j] = cisla[i]
                #print(cisla[j],cisla[i])
                j += 1
                i -= 1
                       
        else:
            stred = (dlzka//2)
            print(cisla[stred],stred)
            
            j = stred + 1
            i = stred - 1
            
            if cisla[stred-1] == "9":
                zmena = 9
                cisla[stred] = str(zmena)
                #j += 1
                i -= 1
                #print(cisla)
            else:
                zmena = int(cisla[stred]) + 1
                cisla[stred] = str(zmena)
                
                #print("2",cisla)
            
            for cislo1 in cisla:
                if dlzka == pocet:
                    break
                if j == dlzka:
                    break
                cisla[j] = cisla[i]
                j += 1
                i -= 1
                
                #print(cisla)
                
    if dlzka == pocet:
        
        vysledok = int(cislo) + 2
        print(vysledok)
            
    else:
        for cislo1 in cisla:
            vysledok += str(cislo1)
        if zvysok == 0:
            vysledok += str(cisla[0])
            print(vysledok)
        else:
            print(vysledok)

    """if zvysok == 0:
            vysledok += str(cisla[0])
            print(vysledok)"""
    cisla = []
    stred = 0
    zvysok = 0
    dlzka = 0
    zostatok = []
    zmena = 0
    vysledok = ""
    j = 0
    i = 0
    pocet = 0
    pocet_cyklov -= 1
