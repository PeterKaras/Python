pocet_cyklov = int(input("Zadajte pocet cyklov: "))
listy = []
pomocna = ""
vysledok = ""
vysledok1 = ""

while pocet_cyklov != 0:
    cisla = input("Zadajte cisla: ") + " "
    for cislo in cisla:
        if cislo == " ":
            listy.append(pomocna)
            pomocna = ""
        else:
            pomocna += cislo
    print(listy)
            
    vysledok = listy[0] * int(listy[1])
    vysledok1 = listy[2] * int(listy[3])
    dlzka = len(vysledok)
    dlzka1 = len(vysledok1)
    if dlzka < dlzka1:
        print("mensie")
    elif dlzka == dlzka1:
        print("rovne")
    else:
        print("vacsie")
        
    #print(listy)
    listy = []
    vysledok = ""
    vysledok1 = ""
    pomocna = ""
    dlzka = 0
    dlzka1 = 0
    pocet_cyklov -= 1
