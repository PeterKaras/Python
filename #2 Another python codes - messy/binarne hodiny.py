pocet_cyklov = int(input("Zadajte pocet cyklov: "))
i = 0
j = 0
cas = []
docasne = ""
vysledok = []
hviezdy = "." * 6
hladatel = 8
porovnanie = []
docasny_vysledok = 0
celkovy_vysledok = ""
pocet = 1

for pismeno in hviezdy:
    vysledok.append(pismeno)

#print(vysledok)

while pocet_cyklov != 0:
    cas1 = input("Zadajte cas v digitalnom sposobe: ") + ":"
    for pismeno in str(cas1):
        if pismeno == "0" and i == 0:
            pass
        elif pismeno == ":":
            cas.append(docasne)
            docasne = ""
            i = 0
            pass
        elif pismeno == " ":
            pass
        else:
            docasne += pismeno
            
        i += 1
    #print(cas)
    i = 0
    docasne = ""

    for cislo in range(4):
        for pismeno in cas:
            
            for pismeno1 in str(cas[i]):
                if pismeno1 == "-":
                    pass
                else:
                    #print(pismeno1)
                    porovnanie.append(int(pismeno1))
                
            #print("i:",i,"Hladatel:",hladatel, porovnanie)            
            if hladatel <= porovnanie[0]:
                if int(cas[i])> 9:
                    docasny_vysledok = int(cas[i]) - (hladatel*10)
                    vysledok[j] = "*"
                    cas[i] = str(docasny_vysledok)
                    
            if hladatel > int(porovnanie[-1]):
                pass            
            else:
                docasny_vysledok = int(cas[i]) - hladatel
                #print(docasny_vysledok)
                
                vysledok[j+1] = "*"
                #print("normal",vysledok)
                cas[i] = str(docasny_vysledok)
                #print("2",cas)

            if int(cas[i])/10 == hladatel:
                vysledok[j] = "*"
                cas[i] = "0"
                #print(cas)
                
                                    
            j += 2 
            i += 1
            porovnanie = []
        j = 0   
        i = 0
        
        celkovy_vysledok += str(hladatel)
        
        for pismeno3 in vysledok:
            celkovy_vysledok += pismeno3
        #print(vysledok)
        print(celkovy_vysledok)
        celkovy_vysledok = ""
        hladatel //= 2
        vysledok = []
        for pismeno in hviezdy:
            vysledok.append(pismeno)

    
    
    i = 0
    j = 0
    cas = []
    docasne = ""
    vysledok = []
    pocet_cyklov -= 1
    hladatel = 8
    porovnanie = []
    docasny_vysledok = 0
    celkovy_vysledok = ""
    for pismeno in hviezdy:
        vysledok.append(pismeno)
