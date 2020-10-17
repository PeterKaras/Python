pocet_cyklov = int(input("Zadajte pocet cyklov: "))
listy = []
vyska = []
sirka = []
docasne = ""
pomocna = ""
vysledok = 0
vysledok1 = 0
slovo = ""
cislo1 = 0

while pocet_cyklov != 0:
    cisla = input("Zadajte cisla: ") + " "
    pokyny = input("Zadajte vase pokyny: ").upper()
    for cislo in cisla:
        if cislo == " ":
            listy.append(docasne)
            docasne = ""
        else:
            docasne += cislo
            
    #print(listy)

    for pismeno in pokyny:
        if pismeno == "L" or pismeno == "P":
            sirka.append(pismeno)
        else:
            vyska.append(pismeno)
    #print(sirka)
    #print(vyska)
    
    docasne = ""
    pomocna = ""
    
    for pismeno in sirka:
        dlzka = len(sirka)
        if dlzka == 1:
            vysledok += 1
        else:
            if pomocna == "":
                pomocna = pismeno
                docasne = pomocna
            
            elif docasne != pomocna:
                #print("BE")
                cislo1 -= 1
                if cislo1 == 0:
                    docasne = pomocna
                vysledok -= 1
            
            elif docasne == pomocna:
                #print("BLUH")
                vysledok += 1
                cislo1 += 1
            
            pomocna = pismeno
            #print("1.",vysledok)
        if (vysledok) == int(listy[1]):
            slovo = "mantinel"
            break
        
    pomocna = ""
    docasne = ""
    cislo1 = 0
    
    for pismeno in vyska:
        #print(docasne,pomocna)
        dlzka1 = len(vyska)
        if dlzka1 == 1:
            vysledok1 += 1 
        else:
            if pomocna == "":
                #cislo1 += 1
                pomocna = pismeno
                docasne = pomocna
            
            elif docasne != pomocna:
                #print("BE")
                cislo1 -= 1
                if cislo1 == 0:
                    docasne = pomocna
                vysledok1 -= 1
            
            elif docasne == pomocna:
                #print("BLUH")
                vysledok1 += 1
                cislo1 += 1
        
            pomocna = pismeno
            #print("2.",vysledok1)

        
        if vysledok1 == int(listy[0]):
            slovo = "mantinel"
            break

    if slovo == "mantinel":
        print("Mantinel")
    else:
        print("v poriadku")
        
    listy = []
    vyska = []
    sirka = []
    docasne = ""
    pomocna = ""
    vysledok = 0
    vysledok1 = 0
    slovo = ""
    cislo1 = 0   
    pocet_cyklov -= 1
    
