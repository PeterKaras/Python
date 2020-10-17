pocet_cyklov = int(input("Zadajte pocet priestorov: "))
priestor = []
znak = []
i = 0
index = []
j = 0
k = 0
slovo = "koniec"
celok = []
pocet = 0
vyska = 0
sirka = 0

while pocet_cyklov != 0:
    priestor1 = input("Zadajte rozmery priestoru: ")
    for cislo in str(priestor1):
        if cislo == " ":
            pass
        else:
            priestor.append(int(cislo))
            
    #print(priestor)
    for cislo in range(priestor[0]):
        znaky = input("Zadajte vase znaky atramentom: ")
        for pismeno in znaky:
            znak.append(pismeno)
            celok.append(pismeno)
    
        for pismeno in znak:
            if znak[i] == ".":
                pass
            else:
                index.append(str(i))
                
            i += 1
        znak = []
        i = 0
        
    for j in range(len(index)-1,0,-1):
        for k in range(j):
            if index[k] > index[k+1]:
                temp = index[k]
                index[k] = index[k+1]
                index[k+1] = temp
    #print(index)
    i = 0
    k = 0
    j = 0
    for cislo in index:
        for cislo1 in index:
            if j <= i:
                j += 1
                pass
            else:
                if index[i] == index[j]:
                    slovo = ""
                    break
                else:
                    slovo = "koniec"
        if slovo == "":
            break
        i += 1
        j = 0

    #print(slovo)
    i = 0
    j = 0
    vyska = priestor[0]
    sirka = priestor[1]
    vyska1 = priestor[0]
    for pismeno in range(priestor[0]):
        if slovo == "koniec":
            break
        for pismeno in range(priestor[1]):
            if celok[i] == ".":
                pass
            else:
                if celok[i] == "^":
                    vyska1 += 1
                    if vyska1 > priestor[0]:
                        pocet += 1
                        #print(pocet,celok[i])


                elif celok[i] == "v":
                    vyska1 -= 1
                    if vyska1 < 0:
                        #print(vyska1,priestor[0])
                        pocet += 1
                        #print(pocet,celok[i])

                elif celok[i] == ">":
                    if j == priestor[1]:
                        pocet += 1
                        #print(pocet,celok[i])

                elif celok[i] == "<":
                    if j == 0:
                        pocet += 1
                        #print(pocet,celok[i])
                
                
            i += 1
            j += 1
        j = 1
        vyska -= 1
        vyska1 = vyska
        
    if slovo == "koniec":
        print("-1")
    elif pocet == 0:
        print("0")
    else:
        print(pocet)
    priestor = []
    znak = []
    i = 0
    index = []
    j = 0
    k = 0
    slovo = "koniec"
    celok = []
    pocet = 0
    vyska = 0
    sirka = 0
    
    pocet_cyklov -= 1
