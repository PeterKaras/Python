pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla = []
cisla2 = []
i = 0
j = 0
k = 0
vynasobene = 0
koniec = ""
pocet = 0
zostatok = ""
vysledok = []
zostatok1 = -1
pocet1 = 0
porovnanie = []
slovo = ""


while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet cisiel: "))
    cisla1 = input("Zadajte objem tekutiny: ")
    for cislo in cisla1:
        if cislo == " ":
            pass
        else:
            cisla2.append(cislo)                                                                                                                                                                                               

    #print(cisla2)


    for i in range(len(cisla2)-1,0,-1):
        for j in range(i):
            if cisla2[j] > cisla2[j+1]:
                temp = cisla2[j]
                cisla2[j] = cisla2[j+1]
                cisla2[j+1] = temp

    #print("Zoradene",cisla2)
    i = 0
    j = 0
    dlzka = len(cisla2)
    for cislo in cisla2:
        if int(cislo) == int(cisla2[k+1]):
            porovnanie.append(cislo)
    
        pocet1 += 1
        if pocet1 == (dlzka-1):
            break
        
    #print(porovnanie)
    #print(cisla)
    
    cisla = cisla2
    #print(cisla)
    for cislo in cisla:
    
        cisla = []
        for pismeno in cisla2:
            cisla.append(pismeno)
        #print(cisla[i],",DOPICE")
        vynasobene = int(cisla[i])*2
        if zostatok == cisla[i]:
            pass
        else:
            for cislo1 in cisla:
                #print(cislo1,vynasobene)
                if int(cisla[j]) == vynasobene:
                    cisla[j] = " "
                    #print("Som tu")
                    koniec = "koniec"
                    break
                j += 1
                
            j = 0
            for cislo1 in cisla:
                if cislo1 == " ":
                    pass
                else:
                    vysledok.append(cislo1)
                    
            #print(cisla)        
            if koniec == "koniec":
                for cislo1 in porovnanie:
                    if int(cisla[i]) == int(porovnanie[k]):
                        #print("mozes")
                        slovo = "mozes"
                        break
                    k +=1
                    
                if slovo == "mozes":
                    
                    koniec = ""
                    #print("koniec",koniec)
                    
                    for cislo1 in vysledok:
                        #print(cislo1,vynasobene)
                        if int(cislo1) == vynasobene:
                            koniec = "koniec"
                            break
                        #print("J",j)
                        j += 1

            if koniec == "koniec":
                pass
            else:
                pocet += 1
                #print("Zapocital som")
        #print(cisla)
        zostatok = cisla[i]
        i += 1
        k = 0
        j = 0
        koniec = ""
        slovo = ""
        vysledok = []
    
        
    print(pocet)    
    cisla = []
    cisla2 = []
    i = 0
    j = 0
    k = 0
    vynasobene = 0
    koniec = ""
    pocet = 0
    zostatok = ""
    vysledok = []
    zostatok1 = -1
    pocet1 = 0
    porovnanie = []
    slovo = ""  
    pocet_cyklov -= 1
