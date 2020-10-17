cely_cyklus = int(input("Zadajte pocet cyklov: "))
listy = []
cisla = []
cislo = 0
cisla1 = []
i = 0
zvysok = 0
docasne = 0
slovo = ""
zvysok1 = 0

while cely_cyklus != 0:
    riadky = int(input("Zadajte pocet riadkov v jednom cykle: "))
    znaky = int(input("Zadajte pocet znakov v riadkoch: "))
    for i in range(riadky):
        i = 0
        cisla = []
        cisla1 = []
        listy = []
        kalibracia = input("Zadajte znaky: ")
        dlzka = len(kalibracia)
        #print(dlzka)
        if znaky != dlzka:
            break
        
        for pismeno in kalibracia:
            listy.append(pismeno)
        #print(listy)
        for pismeno in listy:
            if listy[i] == "C":
                cislo = i
                cisla.append(cislo)
            #print(cisla)
            
            if listy[i] == "B":
                cislo = i
                cisla1.append(cislo)
        
            i += 1

        if cisla != []:
    
            zvysok1 = int(cisla[0])%2
            docasne = zvysok1
            for cislo in cisla:
                zvysok1 = int(cislo)%2
                if zvysok1 == docasne:
                    pass
                else:
                    slovo = "koniec"
                    break
        
        if cisla1 != []:
            zvysok = int(cisla1[0])%2
            if cisla != []:
                if zvysok == zvysok1:
                    slovo = "koniec"
    
            docasne = zvysok
            for cislo in cisla1:
                if slovo == "koniec":
                    break
                zvysok = int(cislo)%2
                if zvysok == docasne:
                    pass
                else:
                    slovo = "koniec"
                    break
        if slovo == "koniec":
            break
    if znaky != dlzka:
        print("Skus znovu")
    elif slovo == "koniec":
        print("NEda sa to spravit")
    elif slovo == "":
        print("Da sa")
    
            
       
        
    docasne = ""
    predosle = ""
    listy = []
    zvysok = 0
    slovo = ""
    cisla = []
    cislo = 0
    cisla1 = []
    cely_cyklus -= 1 
