pocet_cyklov = int(input("Zadajte pocet beanii (cyklov): "))
cisla = []
j = 0
i = 0
delitel = 2
b = 0
a = 0
c = 0
vysledok = []
docasne = []
vysledok1 = []
zostatok = 0

while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet cisiel: "))
    cisla1 = input("Zadajte vase cisla: ")
    for cislo in str(cisla1):
        if cislo == " ":
            pass
        else:
            cisla.append(int(cislo))

    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if cisla[j] > cisla[j+1]:
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
                
    i = 0
    j = 0
                
                
    #print(cisla)
    for cislo in cisla:
        for cislo1 in cisla:
            if j <= i:
                j += 1
                pass
            else:
                a = cisla[i]
                b = cisla[j]
                if a == b:
                    pass
                else:
                    while b != 0:
                        if a >= b:
                            a = a - b
                        else:
                            c = a
                            a = b
                            b = c

                    if (a-b) == 1:
                        pass
                    else:
                        docasne.append(a-b)
                    if docasne == []:
                        vysledok.append(-1)
                    
                    for cislo2 in docasne:
                        vysledok.append(cislo2)
                    docasne = []
  
                j += 1
        j = 0
        i += 1
    
        #print(vysledok)
    j = 0
    i = 0
    for i in range(len(vysledok)-1,0,-1):
        for j in range(i):
            if vysledok[j] > vysledok[j+1]:
                temp = vysledok[j]
                vysledok[j] = vysledok[j+1]
                vysledok[j+1] = temp


    for cislo in vysledok:
    
        if cislo == zostatok:
            pass
        else:
            vysledok1.append(cislo)
            
       
        zostatok = cislo

        #print(vysledok1)

    dlzka = len(vysledok1)
    print(dlzka)
    cisla = []
    j = 0
    i = 0
    delitel = 2
    b = 0
    a = 0
    c = 0
    vysledok = []
    docasne = []
    vysledok1 = []
    zostatok = 0
    pocet_cyklov -= 1
