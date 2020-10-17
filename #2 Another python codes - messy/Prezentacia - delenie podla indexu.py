pocet_cyklov = int(input("Pocet cyklov: "))
cisla = []
pocet = 0
vysledok = []
index = []
docasne = []
index1 = 0
index2 = 0
vysledne = []
dlzka = 0
zadok = []
predok = []
jednotky1 = 0
jednotky = 0
slovo = ""
i = 0
k = 0
j = 0
dobre = 0

while pocet_cyklov != 0:
    cislo1 = input("Zadajte cisla: ")
    for cislo in str(cislo1):
        cisla.append(cislo)
        vysledok.append(cislo)
        
    if cisla[-1] == "0":
        cisla.append("1")
        vysledok.append("1")
        #pocet += 1
        
    docasne = cisla
    #print(docasne)

    j = 0
    j = len(docasne)-1
    #print(j)
    """for pismeno4 in docasne:
        #print(docasne[j])
        if docasne[j] == " ":
            pass
        if docasne[j] == "1":
            jednotky += 1
        else:
            break
        j -= 1"""
        
    j = 0
    
    for k in range(len(cisla)-1,0,-1):
        for j in range(k):
            if int(vysledok[j]) > int(vysledok[j+1]):
                temp = vysledok[j]
                vysledok[j] = vysledok[j+1]
                vysledok[j+1] = temp

    j = 0
    i = 0
    k = 0
    for pismeno in cisla:
        if cisla[j] == "1":
            index.append(str(j))
        j += 1
    #print(index)
    
    j = 0
    for cislo in range(jednotky):
        if i == jednotky:
            #print(i)
            break
        else:
            dobre = dlzka - i
            #print(i)
            for cislo in index:
                if cislo == dobre:
                    pass
                else:
                    slovo = "koniec"
                    break
            i += 1
        if slovo == "koniec":
            break
        
        #print(i)
    #print(slovo)    
    i = 0
    j = 0
    dlzka = len(index)
    #print(index)
    #print(index[-1])
    for pismeno in range(len(index)):
        #print(index)
        for pismeno1 in cisla:
            if i == (dlzka-1):
                break
       
            if index1 == int(index[-1]):
                break
            else:
                index1 = int(index[i])
                #print("Index1",index1)
            
            if i == (dlzka-1):
                break
            else:
                if index1 == int(index[-1]):
                    break
                else:
                    index2 = int(index[i+1])
                    #print("index2",index2)

            j = 0
            for znak in cisla:
                if index1 == 0:
                    pass
                else:
                    predok.append(cisla[j])
                    cisla[j] = " "
                    j += 1
                    if j == int(index1):
                        break
            j = 0
        
            for pismeno3 in cisla:
                if j < int(index2+1):
                    j += 1
                    pass
                else:
                    zadok.append(cisla[j])
                    cisla[j] = " "
                    j += 1
                    
            #print("cisla",cisla)
            #print("predok",predok)
            #print("zadok",zadok)
        
            for pismeno3 in cisla:
                if pismeno3 == " ":
                    pass
                else:
                    vysledne.append(pismeno3)

            #print("vysledne",vysledne)
            
            j = 0
            k = 0

            for k in range(len(vysledne)-1,0,-1):
                for j in range(k):
                    if int(vysledne[j]) > int(vysledne[j+1]):
                        dobre += 1 
                        pocet += 1
                        temp = vysledne[j]
                        vysledne[j] = vysledne[j+1]
                        vysledne[j+1] = temp

            #print("po uprave",vysledne)
            if dobre == 0:
                pass
            else:
                pocet += 1
            cisla = []
            for pismeno3 in predok:
                cisla.append(pismeno3)
            for pismeno3 in vysledne:
                cisla.append(pismeno3)
            for pismeno3 in zadok:
                cisla.append(pismeno3)
            i += 1
            j = 0
            k = 0
            dobre = 0
            predok = []
            zadok = []
            vysledne = []
            #print("cisla",cisla)
            if cisla == vysledok:
                break
        index = []
        for pismeno3 in cisla:
            if cisla[j] == "1":
                index.append(str(j))
            j += 1
        
        j = 0
        i = 0
        
    #print(jednotky)
    jednotky1 = cisla.count("1") - jednotky
    
    print(pocet)
    cisla = []
    pocet = 0
    vysledok = []
    index = []
    docasne = []
    index1 = 0
    index2 = 0
    vysledne = []
    dlzka = 0
    zadok = []
    predok = []
    jednotky1 = 0
    jednotky = 0
    slovo = ""
    i = 0
    k = 0
    j = 0
    pocet_cyklov -= 1
