pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla = []
cisla2 = []
x = []
y = []
i = 0
j= 0
pocet = 0
vysledok = 0
vysledok1 = 0
pravde = 0
cislo1 = ""

while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet dvojic na zadavanie: "))
    for cislo in range(pocet_cisiel):
        cisla1 = input("Zadajte cisla: ")
        for cislo in str(cisla1):
            cislo1 += cislo
            if cislo1 == " ":
                #cislo1 = ""
                pass
            if cislo == "-":
                pass
            else:
                cisla.append(cislo1)
                cislo1 = ""
    cislo1 = ""
    #print(cisla)
    for cislo in cisla:
        if cislo == " ":
            pass
        else:
            cisla2.append(cislo)
    #print(cisla2)       
    for cislo in cisla2:
        if i % 2 == 0 :
            x.append(cislo)
        else:
            y.append(cislo)
        i += 1 
        
        
    #print(x)
    #print(y)
    i = 0
    j = 0
    dlzka = len(x)
    for cislo in x:
        
        vysledok = int(x[i]) + int(x[i+1])
        vysledok1 = int(y[i]) + int(y[i+1])
        #print(x[i],y[i],x[i+1],y[i+1])
        #print(vysledok,vysledok1)
        i += 1
        if vysledok == vysledok1:
            pocet += 1
        if i == (dlzka-1):
            break
        
            
        vysledok = 0
        vysledok1 = 0
        
    if pocet == 0:
        pravde = 0
        pass
    else:
        pravde = pocet/pocet_cisiel
        print(pocet,pocet_cisiel)
    print(pravde)

    cisla = []
    x = []
    y = []
    i = 0
    pocet = 0
    vysledok = 0
    vysledok1 = 0
    pravde = 0
    cisla2 = []
    j = 0
    cislo1 = ""
    pocet_cyklov -= 1
    
    
