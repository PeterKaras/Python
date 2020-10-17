pocet_cyklov = int(input("Zadajte pocet vkladov/vyberov: "))
cisla = []
inkrement = 0
rozdiel = 0
cislo1 = ""
pocet = 0


while pocet_cyklov != 0:
    cisla1 = input("Zadajte cisla: ") + " "
    for cislo in str(cisla1):
        if cislo == " ":
            cisla.append(int(cislo1))
            cislo1 = ""
            pass
        else:
            cislo1 += cislo

    #print(cisla)
    inkrement = cisla[1]
    while inkrement != cisla[2]:

        rozdiel = inkrement - cisla[0]
        inkrement += rozdiel
        #print(inkrement)
        if inkrement >= cisla[2]:
            pocet += 1
            break
        else:
            pocet += 1
            continue 


    print(pocet)
    cisla = []
    inkrement = 0
    rozdiel = 0
    cislo1 = ""
    pocet = 0
    pocet_cyklov -= 1
    
