pocet_cyklov = int(input("Zadajte pocet cyklov: "))
zaciatok = []
spojovnik = ""
pocet = 0
ulohy = []
zavislosti = []
cisla= []
stare = ""
indexy = []
j = 0
zoradenie = []
celkove = []
slovo = "ok"
stare1 = 0

while pocet_cyklov != 0:
    cislo = input("Zadajte pocet uloh a zavislosti: ").strip()
    cislo += " "
    for cislo1 in cislo:
        if cislo1 == "-":
            spojovnik += cislo1
        elif cislo1.isdigit() == True:
            spojovnik += cislo1
        elif cislo1 == " ":
            zaciatok.append(spojovnik)
            spojovnik = ""
        else:
            continue

    print(zaciatok)        

    for i in range(int(zaciatok[1])):
        cislo = input("Zadajte pocet uloh a zavislosti: ").strip()
        cislo += " "
        for cislo1 in cislo:
            if cislo1 == "-":
                spojovnik += cislo1
            elif cislo1.isdigit() == True:
                spojovnik += cislo1
            elif cislo1 == " ":
                if pocet == 0:
                    ulohy.append(spojovnik)
                    spojovnik = ""
                    pocet += 1
                elif pocet == 1:
                    zavislosti.append(spojovnik)
                    pocet = 0
                    spojovnik = ""
            else:
                continue

    print(ulohy)
    print(zavislosti)

    for znak in ulohy:
        if znak == stare:
            pass
        else:
            cisla.append(znak)   
        stare = znak

    #print(cisla)
    dlzka = len(cisla)
    i = 0

    for cislo in range(dlzka):
        for znak in ulohy:
            if znak == cisla[i]:
                indexy.append(j)

            j += 1
        j = 0
        
        for znak in range(len(indexy)):
            index = indexy[j]
            zoradenie.append(zavislosti[index])
            j += 1

        #print(zoradenie)
        for k in range(len(zoradenie)-1,0,-1):
            for p in range(k):
                if int(zoradenie[p]) > int(zoradenie[p+1]):
                    temp = zoradenie[p]
                    zoradenie[p] = zoradenie[p+1]
                    zoradenie[p+1] = temp

        print(zoradenie)
        for pismeno in zoradenie:
            celkove.append(pismeno)
        indexy = []
        zoradenie = []
        i += 1
        j = 0

    i = 0
    j = 0
    k = 0
    
    print(celkove)
    dlzka1 = len(celkove)
    for cislo in ulohy:
        if slovo != "ok":
            break
        elif stare1 < int(celkove[i]):
            pass
        elif stare1 == int(celkove[i]):
            if int(ulohy[i]) >  int(ulohy[i-1]):
                pass
            elif int(ulohy[i]) <  int(ulohy[i-1]):
                slovo = "break"
                break
        elif stare1 > int(celkove[i]):
            slovo = "break"
            break
        stare1 = int(celkove[i])
        i += 1
        if i == dlzka1:
            break

    if slovo == "ok":
        print("V poriadku")
    elif slovo == "break":
        print("Prepracovat")
        
    zaciatok = []
    spojovnik = ""
    pocet = 0
    ulohy = []
    zavislosti = []
    cisla = []
    stare = ""
    indexy = []
    j = 0
    zoradenie = []
    celkove = []
    slovo = "ok"
    stare1 = 0
    pocet_cyklov -= 1
