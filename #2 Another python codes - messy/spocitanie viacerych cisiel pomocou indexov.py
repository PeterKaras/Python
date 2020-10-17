cas1 = [8,12,16,20,24]
cas = [12,20,24,16,8]
zabavnost = [10,10,10,10,3]
pomocna = [6,12,16,20,24]

limit = 40
dlzka = len(cas1)
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
sucet_l = []
indexy = []
sucet_z = 0
maxi_z = 0
mini_c = 500000

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
                if sucet < limit:
                    pridanie.append(cas1[j])
                if sucet > limit:
                    sucet -= cas1[j]
                    break
                    
            j += 1
            
        j = posunutie
        posunutie += 1
        sucet_l.append(sucet)
        
        for pismeno in pridanie:
            for pismeno1 in cas:
                if cas[k] == pridanie[p]:
                    indexy.append(k)
                    break
                k += 1   
            k = 0
            p += 1

        p = 0
        #print("i",indexy)
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
        
    #print("j2",j,dlzka,i)
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


























        
"""if dlzka == 2:
            sucet += cas1[j]
            pocet += 1
            if sucet > limit:
                sucet -= cas1[j]
                pocet -= 1
                slovo = "koniec"

            j += 1
            if j == (dlzka-1) or slovo == "koniec":
                cisla.append(sucet)
                pocet_c.append(pocet)
                break
            
        for znak2 in cas1:
            if k <= j:
                k += 1
                pass
            else:
                sucet = sucet + cas1[k]
                print("Sucet2",sucet)
                if sucet > 50:
                    sucet -= cas1[k]
                    slovo = "davaj"
                    print("kokot",sucet)
                else:
                    cisla.append(cas1[k])
                    print("CISLA",cisla)
                    pocet += 1
                    print(pocet)

                if k == (dlzka-1):
                    pocet = 2
              
                print(i,j,k)
                k += 1
                    
        k = 0
        cisla = []
        slovo = ""
        j += 1
        if j == (dlzka):
            break
        
    i += 1
    k = 0
    j = i + 1
    if j == (dlzka-1):
        break


print(cisla)
print(pocet_c)
"""


















        
"""sucet = cas1[i] + cas1[j]
        cisla.append(cas1[i])
        cisla.append(cas1[j])
        print("SUCET",sucet)
        for znak2 in cas1:
            if k <= j:
                k += 1
                pass
            else:
                sucet = sucet + cas1[k]
                print("Sucet2",sucet)
                if sucet > 50:
                    sucet -= cas1[k]
                    slovo = "davaj"
                    print("kokot",sucet)
                else:
                    cisla.append(cas1[k])
                    print("CISLA",cisla)
                    pocet += 1
                    print(pocet)


                if k == (dlzka-1) or slovo == "davaj":
                    if sucet > maxi and pocet > maxi_pocet:
                        vysledne_cisla = []
                        vysledne_cisla = cisla
                        #cisla = []
                        #print(vysledne_cisla)
                        maxi = sucet
                        maxi_pocet = pocet
                        #print("M",maxi,"pocet",maxi_pocet)
                        
                if k == (dlzka-1):
                    pocet = 2
              
                print(i,j,k)
                k += 1
                
        k = 0
        cisla = []
        slovo = ""
        j += 1
        if j == (dlzka):
            break
    i += 1
    #slovo = ""
    #cisla = []
    k = 0
    j = i + 1
    if j == (dlzka-1):
            break"""

#print(maxi,maxi_pocet)
