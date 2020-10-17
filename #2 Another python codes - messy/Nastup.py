pocet_cyklov = int(input("Zadajte pocet cyklov :"))
sirka1 = []
sirka2 = []
indexy = []
pomocna = []
vysledne = []
dalsie = []
s1 = []
s2 = []
bodky = 0
i = 0
j = 0
pocet = 0
zvysok = 0
slovo = ""
slovo1 = ""
zvysok1 = 0
index = 0
pomocna1 = []
neparne = 0
neparne1 = 0
while pocet_cyklov != 0:
    sirka = int(input("Zadajte sirku obrazca :"))
    for line in range(1):
        znak1 = input("Zadajte znaky :")
        znak2 = input("Zadajte znaky :") 
        
        for pismeno in znak1:
            sirka1.append(pismeno)
        for pismeno in znak2:
            sirka2.append(pismeno)
        i = 0
        
        dlzka = len(sirka1)-1
        
        for pismeno in sirka1:
            if sirka1[i] == "." and sirka2[i] == ".":
                #print(i,dlzka)
                if i == (dlzka):
                    #print(i,dlzka)
                    break
                elif sirka1[i+1] == "#" and sirka2[i+1] == "#":
                    slovo1 = "koniec"
                    #print("Buh")
                    break  
            elif sirka1[i] == "." and sirka2[i] == ".":
                if sirka1[i-1] == "#" and sirka2[i-1] == "#":
                    #print(i)
                    i += 1
                    pass  
            else:
                i += 1
                #print(i)
                continue
        
        dlzka = len(sirka1)-1
        i = dlzka
        for pismeno in sirka1:
            if sirka1[i] == "." and sirka2[i] == ".":
                sirka1[i] = " "
                sirka2[i] = " "
                i -= 1
            else:
                break
        #print(sirka1)
        #print(sirka2)
        
        s1 = sirka1
        s2 = sirka2
        sirka1 = []
        sirka2 = []
        
        for pismeno in s1:
            if pismeno == " ":
                pass
            else:
                sirka1.append(pismeno)

        for pismeno in s2:
            if pismeno == " ":
                pass
            else:
                sirka2.append(pismeno)
        
        if slovo1 == "koniec":
            break
        i = 0
        #print(sirka1)
        dlzka = len(sirka1)
        #print(sirka2)
        
        for pismeno in sirka1:
            if slovo1 == "koniec":
                #print("2buh")
                break
            if sirka1[i] == ".":
                #print(i)
                indexy.append(str(i))
                i += 1
            else:
                i += 1
                continue
                
        #print(indexy)
        i = 0
        for pismeno in sirka2:
            if slovo1 == "koniec":
                #print("3buh")
                break
            if pismeno == ".":
                indexy.append(str(i))
                i += 1
            else:
                i += 1
                continue
        i = 0
        j = 0
        print("1",indexy)
        for i in range(len(indexy)-1,0,-1):
            for j in range(i):
                 if int(indexy[j])>int(indexy[j+1]):
                    temp = indexy[j]
                    indexy[j] = indexy[j+1]
                    indexy[j+1] = temp

        
        i = 0
        j = 0
        print("2",indexy) 
        for cislo1 in indexy:
            if slovo1 == "koniec":
                #print("5buh")
                break
            for cislo in indexy:
                if j <= i:
                    j += 1
                    pass
                else:
                    if indexy[i] == indexy[j]:
                        slovo1 = "koniec"
                        indexy[j] = " "
                        print(indexy)
                        break
                    else:
                        j += 1
                        continue
            j = 0
            i += 1

        #print(indexy)
        for cislo in indexy:
            if slovo1 == "koniec":
                #print("6buh")
                break
            if cislo == " ":
                pass
            else:
                vysledne.append(cislo)
        print("v",vysledne)
        i = 0
        j= 0
        print(vysledne)
        
        dlzka = len(vysledne)
        indexy = []

        pomocna1 = sirka1
        #print(pomocna1)
        pomocna = sirka2
        
        #print(indexy)
        
        for pismeno in vysledne:
            if slovo1 == "koniec":
                #print("7buh")
                break
            sirka1 = []
            dalsia = []
            for pismeno in pomocna1:
                sirka1.append(pismeno)
            #print(sirka1)
            index1 = int(vysledne[i])
            i += 1
            
            if i == dlzka:
                break
            else:
                index2 = int(vysledne[i])
            #print(index1,index2)
            
            for pismeno in sirka1:
                if int(index1) == 0:
                    pass
                else:
                    sirka1[j] = " "
                    j += 1
                    if j == (index1):
                        break
            j = 0
            
            for pismeno in sirka1:
                if j < (index2+1):
                    j += 1
                    pass
                else:
                    
                    sirka1[j] = " "
                    j += 1
                #print(sirka1)
                
            for pismeno in sirka1:
                if pismeno == " ":
                    pass
                else:
                    dalsia.append(pismeno)
                    
            #print("s",sirka1)        
            print(dalsia)

            
            
            for pismeno in dalsia:
                if pismeno == "#":
                    pocet += 1
                elif pismeno == ".":
                    zvysok = pocet % 2
                    #print(zvysok,pocet)
                    if zvysok != 0:
                        neparne = zvysok
                        slovo = "koniec"
                    pocet = 0
                    
            #print("s1",sirka1)
            j = 0
            dalsia = []
            for pismeno in sirka2:
                if int(index1) == 0:
                    pass
                else:
                    sirka2[j] = " "
                    j += 1
                    if j == (index1):
                        break
            j = 0
            
            for pismeno in sirka2:
                if j < (index2+1):
                    j += 1
                    pass
                else:
                    
                    sirka2[j] = " "
                    j += 1
            j = 0
            #print(sirka2)
            for pismeno in dalsia:
                if pismeno == "#":
                    pocet += 1
                elif pismeno == ".":
                    zvysok = pocet % 2
                    #print(zvysok,pocet)
                    if zvysok != 0:
                        neparne1 = zvysok
                        slovo = "koniec"
                    pocet = 0
            if neparne != 0 and neparne1 != 0:
                break
                
    if neparne != 0 and neparne1 != 0:
        print("Prepracovat")
    if slovo == "koniec":
        print("Prepracovat")
    elif slovo1 == "koniec":
        print("Prepracovat")
    else:
        print("V poriadku")

    sirka1 = []
    sirka2 = []
    indexy = []
    pomocna = []
    vysledne = []
    dalsie = []
    bodky = 0
    i = 0
    j = 0
    pocet = 0
    zvysok = 0
    slovo = ""
    slovo1 = ""
    zvysok1 = 0
    index = 0
    pomocna1 = []
    neparne = 0
    neparne1 = 0   
    pocet_cyklov -= 1
