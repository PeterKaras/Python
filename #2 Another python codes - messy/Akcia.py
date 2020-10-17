pobocky = int(input("Zadajte pocet pobociek: "))
cisla = []
docasne = []
i = 0
j = 0
celkovy_vysledok = 0
vysledok = 0
zostatok = ""
zostatok1 = ""
spojitko = " "


while pobocky != 0:
    akcie = int(input("Zadajte pocet akcii: "))
    for akcia in range(akcie):
        cislo1 = input("Zadajte trzbu: ") + " "

        for cislo in str(cislo1):
            if cislo == "-":
                spojitko += "-"
            elif cislo.isdigit() == True:
                spojitko += str(cislo)
            elif cislo == " ":
                cisla.append(spojitko)
                spojitko = ""

    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if int(cisla[j]) > int(cisla[j+1]):
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
                
    i = 0
    j = len(cisla)-1
    
    print(cisla)
    for cislo in cisla:
        if cisla[i] == zostatok:
            cisla[i] = " "
            pass
        elif cisla[j] == zostatok1:
            cisla[j] = " "
            
            pass
        else:
            vysledok = int(cisla[i]) - int(cisla[j])
            zostatok = cisla[i]
            zostatok1 = cisla[j]
            cisla[i] = " "
            cisla[j] = " "
            if vysledok < 0:
                vysledok *= -1
            celkovy_vysledok += vysledok
        
        print(cisla)
        print(celkovy_vysledok)
        for pismeno in cisla:
            if pismeno == " ":
                pass
            else:
                docasne.append(pismeno)

        cisla = []
        cisla = docasne
        print("C",cisla)
        j = len(cisla)-1
        docasne = []
        if cisla == []:
            break
    print(celkovy_vysledok)
    cisla = []
    docasne = []
    i = 0
    j = 0
    celkovy_vysledok = 0
    vysledok = 0
    zostatok = ""
    zostatok1 = ""
    pobocky -= 1
