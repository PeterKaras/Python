pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla1 = []
cisla2 = []
i = 0
vysledok = 0
cislo1 = ""
while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet cisiel: "))
    cisla = input("Zadajte cisla: ")
    for cislo in str(cisla):
        cislo1 += cislo
        if cislo1 == " ":
            #cislo1 = ""
            pass
        if cislo == "-":
            pass
        else:
            cisla1.append(cislo1)
            cislo1 = ""
    #print(cisla1)

    for cislo in cisla1:
        if cislo == " ":
            pass
        else:
            cisla2.append(cislo)
    #print(cisla2)        
    for cislo in cisla2:
        
        if int(cisla2[i]) == 0:
            pass
        if i == 0:  
            if int(cisla2[i]) < 0 and int(cisla2[i+1]) > 0:
                #print("Luh")
                pass
        elif vysledok == 0:
            vysledok += int(cisla2[i])
        elif int(cisla2[i]) == 0:
            pass
        else:
            vysledok *= int(cisla2[i])
        i += 1
        
    print(vysledok)
    pocet_cyklov -= 1
    cisla1 = []
    i = 0
    cisla2 = []
    vysledok = 0
        
        
