pocet_cyklov = int(input("Zadajte pocet barov: "))
cisla = []
i = 0
vysledok = []
cislo1 = 0
cislo2 = 0


while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet ziakov: ")) 
    ziaci = input("Zadajte litre: ") + " "
    for cislo in str(ziaci):
        if cislo == " ":
            pass
        else:
            cisla.append(int(cislo))

    print(cisla)

    dlzka = len(cisla)

    for cislo in cisla:
        if i == 0:
            vysledok.append(cislo)
            pass
        elif i == (dlzka-1):
            vysledok.append(cislo)
            pass
        else:
            if i == (dlzka-2):
                vysledok.append(cisla[i-1])
            elif i == 1:
                vysledok.append(cisla[i+1])
            elif cisla[i] < cisla[i+1]:
                if cisla[i] > cisla[i-1]:
                    vysledok.append(cislo)
                elif cisla[i] < cisla[i-1]:
                    vysledok.append(cisla[i]+1)
                else:
                    vysledok.append(cislo)
            elif cisla[i] > cisla[i+1]:
                if cisla[i] > cisla[i-1]:
                    vysledok.append(cislo)
                elif cisla[i] < cisla[i-1]:
                    vysledok.append(cisla[i]+1)
                else:
                    vysledok.append(cislo)
                    
            else:
                pass
        cislo1 = 0
        cislo2 = 0
        i += 1

    print(vysledok)
    cisla = []
    i = 0
    vysledok = []
    cislo1 = 0
    cislo2 = 0
    pocet_cyklov -= 1
