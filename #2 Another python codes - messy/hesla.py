cislo = int(input("Zadajte pocet hesiel, kt budete zadavat: "))
i = 0
j = 0
listy = []
prazdna = ""
docasne = []
prazdne = []
pocet = 1
docasne1 = ""
dlzka = 0

while cislo != 0:
    
    heslo = input("Zadajte heslo: ")
    for pismeno in heslo:
        listy.append(pismeno)
    #print(listy)
    
    for pismeno in listy:#HLAVNY CYKLUS
        listy[i] = " "
        #print(listy)
        
        for pismeno in listy: #VEDLAJSI CYKLUS
            if pismeno == " ":
                continue
            else:
                prazdna += pismeno
        #prazdne.append(prazdna) 
        if docasne == []:
            docasne.append(prazdna)
            #print(docasne) 
        else:
            for slovo in docasne:
                docasne1 = docasne[j]
                #print(docasne[j])
                if prazdna == docasne1:
                    pass
                else:
                    j += 1
                    docasne.append(prazdna)
                    break
            
        #print(docasne)    
        listy = []
        for pismeno in heslo:
            listy.append(pismeno)
            
        prazdna = ""
        i += 1
    
        prazdne = []
        
    dlzka = len(docasne)
    j = 0
    i = 0
    docasne = []
    listy = []
    print(dlzka)
    cislo -= 1 
