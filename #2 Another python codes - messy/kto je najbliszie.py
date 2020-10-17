pocet_cyklov = int(input("Zadajte pocet beanii: "))
vstup = []
cisla = []
i = 0
j = 0
pocet = 0
cislo1 = 0
cislo2 = 0

while pocet_cyklov != 0:
    vstup1 = input("Zadajte pocet ucastnikov a hladany rozdiel vysok v cm: ")
    for cislo in str(vstup1):
        if cislo == " ":
            pass
        else:
            vstup.append(int(cislo))

    print(vstup)

    cisla1 = input("Zadajte vysky: ")

    for cislo in str(cisla1):
        if cislo == " ":
            pass
        else:
            cisla.append(int(cislo))

    print(cisla)

    for cislo in cisla:
        for cislo in cisla:
            if j <= i:
                j += 1
            else:
                cislo1 = cisla[i] - cisla[j]
                if cislo1 < 0:
                    cislo1 *= -1
                if cislo1 == vstup[1]:
                    print(cisla[i],cisla[j])
                    pocet += 1
                j += 1
        i += 1
        j = 0
        
    print(pocet)
    vstup = []
    cisla = []
    i = 0
    j = 0
    pocet = 0
    cislo1 = 0
    cislo2 = 0
    pocet_cyklov -= 1
