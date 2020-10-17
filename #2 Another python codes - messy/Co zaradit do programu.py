pocet_cyklov = int(input("Zadajte pocet beanii: "))
zaciatok = []
zabavnost = []
cas = []
cas1 = []
spojitko = ""
pocet = 0
indexy = []
mini_c = 500000
maxi_z = 0
i = 0 
j = i + 1
k = 0
p = 0
posunutie = 2
maxi = 0
sucet = 0
slovo = ""
cisla = []
pridanie = []
zabavnost2 = []
indexy = []
sucet_z = 0

while pocet_cyklov != 0:
    cislo = input("Zadajte cas a pocet cinnosti: ").strip()
    cislo += " "
    for cislo1 in str(cislo):
        if cislo1 == "-":
            spojitko += "-"
        elif cislo1.isdigit() == True:
            spojitko += str(cislo1)
        elif cislo1 == " ":
            zaciatok.append(spojitko)
            spojitko = ""

    for cislo2 in range(int(zaciatok[1])):
        cislo = input("Zadajte cas a zabavnost: ").strip()
        cislo += " "
        for cislo1 in str(cislo):
            if cislo1 == "-":
                spojitko += "-"
            elif cislo1.isdigit() == True:
                spojitko += str(cislo1)
            elif cislo1 == " ":
                if pocet == 0:
                    cas.append(int(spojitko))
                    pocet += 1
                    spojitko = ""
                else:
                    zabavnost.append(int(spojitko))
                    spojitko = ""
                    pocet = 0

    for pismeno in cas:
        cas1.append(pismeno)
        
    for i in range(len(cas1)-1,0,-1):
        for j in range(i):
            if cas1[j] > cas1[j+1]:
                temp = cas1[j]
                cas1[j] = cas1[j+1]
                cas1[j+1] = temp
    
    i = 0
    j = i + 1
    dlzka = len(cas1)
    while True:
        for znak1 in cas1:
            sucet += int(cas1[i])
            pridanie.append(cas1[i])
            for znak in cas1:
                if j == dlzka:
                    break
                if j <= i:
                    pass
                else:
                    sucet += int(cas1[j])
                    if sucet < int(zaciatok[0]):
                        pridanie.append(cas1[j])
                    if sucet > int(zaciatok[0]):
                        sucet -= cas1[j]
                        break
                    
                j += 1
            
            j = posunutie
            posunutie += 1        
            for pismeno in pridanie:
                for pismeno1 in cas:
                    if cas[k] == pridanie[p]:
                        indexy.append(k)
                        break
                    k += 1   
                k = 0
                p += 1

            p = 0
            for pismeno in indexy:
                index = indexy[p]
                sucet_z += zabavnost[index]
                p += 1

            if sucet_z > maxi_z:
                maxi_z = sucet_z
                mini_c = sucet
            elif sucet_z == maxi_z:
                if mini_c > sucet:
                    mini_c = sucet
            else:
                pass
        
            sucet = 0
            pridanie = []
            p = 0
            k = 0
            sucet_z = 0
            indexy = []
            if j == dlzka:
                break

        i += 1
        j = i + 1
        p = 0
        k = 0
        posunutie = j + 1
        if j == dlzka:
            break
        if i == dlzka:
            break

    print(mini_c,maxi_z)
    zaciatok = []
    zabavnost = []
    cas = []
    cas1 = []
    spojitko = ""
    pocet = 0
    indexy = []
    mini_c = 500000
    maxi_z = 0
    i = 0 
    j = i + 1
    k = 0
    p = 0
    posunutie = 2
    maxi = 0
    sucet = 0
    slovo = ""
    cisla = []
    pridanie = []
    zabavnost2 = []
    indexy = []
    sucet_z = 0
    pocet_cyklov -= 1

    
