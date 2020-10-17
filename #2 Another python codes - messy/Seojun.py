pocet_cyklov = int(input("Zadajte pocet cyklov: "))
cisla = []
porovnanie = []
pomocna = []
temp = 0
i = 0
j = 0
index = 0
index1 = 0
cislo2 = ""
docasne = 0
pocet = 0

while pocet_cyklov != 0:
    pocet_cisiel = int(input("Zadajte pocet cisiel: "))
    for znak in range(1):
        cislo1 = input("Zadajte cisla: ")
        
        for cislo in str(cislo1):
            if cislo == " ":
                pass
            else:
                cislo2 += cislo
                cisla.append(cislo)
                porovnanie.append(cislo)
                
        pomocna = cisla
        
        for i in range(len(porovnanie)-1,0,-1):
            for j in range(i):
                if porovnanie[j]>porovnanie[j+1]:
                    temp = porovnanie[j]
                    porovnanie[j] = porovnanie[j+1]
                    porovnanie[j+1] = temp

        temp = 0            
        docasne = 0
        i = 1
        j = 0
        
        for cislo in cisla:
            if cisla == porovnanie:
                break
            index = cislo2.find(str(i))
            #print(index,cislo2,str(i))
            
            docasne = cisla[j]
            index1 = cislo2.find(str(docasne))
            #print(index1,cislo2,str(docasne))

            temp = cisla[index]
            cisla[index] = str(docasne)
            cisla[j] = str(temp)
            pocet += 1
            i += 1
            j += 1
            cislo2 = ""
            for cislo3 in cisla:
                cislo2 += cislo3
            print(cislo2)        
            #print(cisla)
    cisla = []
    docasne = []
    porovnanie = []
    temp = 0
    i = 0
    j = 0
    index = 0
    index1 = 0
    cislo2 = ""
    docasne = 0

    print(pocet)
    pocet = 0
    pocet_cyklov -= 1
