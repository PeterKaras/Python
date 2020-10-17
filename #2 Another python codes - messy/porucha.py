pocet_cyklov = int(input("Zadajte pocet cyklov: "))
porovnanie = []
slovo2 = []
pismeno = ""
i = 0
koniec = ""
hladane_slovo = ""
pocet = 0
pocet1 = 0
zistenie = []
j = 0
p = 0
rozklad = []
maxi = 0
k =0
l = 0
hladat = 0
pokusy = []
vysledok = 0
cisla = []
index = 0
docasne = []


while pocet_cyklov != 0:
    sady = int(input("Zadajte pocet sad na zadavanie: "))
    for cislo in range(sady):
        slovo = input("Zadajte slovo: ").lower()
        for slovo1 in slovo:
            if slovo1 == pismeno:
                zistenie.append(slovo1)
                pass
            else:
                porovnanie.append(slovo1)
                zistenie.append(slovo1)
                
            pismeno = slovo1
            
        zistenie.append(".")    
        pismeno = ""
        
        #print(porovnanie)
        #print(zistenie)
        dlzka = len(zistenie)
        
        if i == 0:
            slovo2 = porovnanie
            
        #print("slovo2",slovo2)   
        if slovo2 == porovnanie:
            pass   
        else:
            koniec = "koniec"
        porovnanie = []
        j = 0
        i += 1

    if koniec == "koniec":
        print("-1")
    elif sady == 1:
        print("0")
    else:
        for pismeno2 in slovo2:
            pismeno = slovo2[p]
            #print(pismeno)
            for pismeno1 in zistenie:
                if pismeno1 == pismeno:
                    #rozklad.append(pismeno)
                    #print(pismeno1)
                    if pocet1 == 0:
                        rozklad.append(pismeno)
                        #print("Heh")
                        if zistenie[index] != zistenie[index+1]:
                            zistenie[index] = " "
                            pocet1 = 1
                            #rozklad.append(".")
                
                if zistenie[index] == ".":
                    #print("HUHH")
                    rozklad.append(".")
                    pocet1 = 0
                
                index += 1
                
                
               
            #print("r",rozklad)    
            for pismeno1 in rozklad:
                if pismeno1 == pismeno:
                    pocet += 1
                else:
                    cisla.append(pocet)
                    pocet = 0

            #print(cisla)
            for k in range(len(cisla)-1,0,-1):
                for l in range(k):
                    if cisla[l]>cisla[l+1]:
                        temp = cisla[l]
                        cisla[l] = cisla[l+1]
                        cisla[l+1] = temp

            #print("c",cisla)
            k = 0
            for cislo in rozklad:
                cislo1 = cisla.count(k)
                if cislo1 > maxi:
                    maxi = cislo1
                    hladat = k

                k += 1

           # print(maxi, hladat)
            for cislo in cisla:
                if cislo == hladat:
                    pass
                else:
                    if cislo < hladat:
                        cislo1 = hladat - cislo
                    else:
                        cislo1 = cislo - hladat
                    pokusy.append(cislo1)
        
            p += 1
            index = 0
            pocet1 = 0
            #print(rozklad)
            rozklad = []
            cisla = []
            maxi = 0
            index = 0
            
        #print(pokusy) 
        for cislo in pokusy:
            vysledok += cislo
            
        print(vysledok)
    pocet_cyklov -= 1
    porovnanie = []
    slovo2 = []
    pismeno = ""
    i = 0
    koniec = ""
    hladane_slovo = ""
    pocet = 0
    pocet1 = 0
    zistenie = []
    j = 0
    p = 0
    rozklad = []
    maxi = 0
    k =0
    l = 0
    hladat = 0
    pokusy = []
    vysledok = 0
    cisla = []
    index = 0
    docasne = []
