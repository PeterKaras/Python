pocet = int(input("Zadajte pocet cyklov: "))
i = 0
listy = []
index = []
j = 0
vysledok = []
pocet_bodiek = 0
bodky = []
iba = 0
zvysok = 0

while pocet != 0:
    polka = input("Zadajte vase znaky: ")
    for pismeno in polka:
        listy.append(pismeno)
        
    for pismeno in listy:
        if pismeno == "s":
            index.append(i)
        if pismeno == ".":
            iba += 1
  
        i += 1
    print(listy)
    print(index)
    
    dlzka = len(index)
    
    if dlzka != 0:
        zvysok = dlzka%2
        #print(zvysok)
        
        pouzitelne = (dlzka//2)-1
        print(pouzitelne)
        
        index = index[pouzitelne]
        print(index)
        
        for pismeno in listy:
            if zvysok != 0:
                break
            listy[j] = " "
            j += 1
            if j == (index+1):
                break
            
        print(listy)
        for pismeno in listy:
            if zvysok != 0:
                break
            if pismeno == " ":
                pass
            else:
                vysledok.append(pismeno)

        for pismeno in vysledok:
            if zvysok != 0:
                break
            #print(pismeno)
            if pismeno == ".":
                pocet_bodiek += 1
            else:
                break
        
    if zvysok != 0:
        print("0")
    elif dlzka != 0:
        print(pocet_bodiek+1)
    else:
        print(iba+1)

    i = 0
    listy = []
    index = []
    j = 0
    iba = 0
    vysledok = []
    pocet_bodiek = 0
    pocet -= 1
