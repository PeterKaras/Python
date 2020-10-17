cisla = ["1","2","3"]
nahrada = ["1","2","3"]
i = 0
j = 1
k = len(cisla)-1
sucet = 0
sucet1 = 0
posuvatel = 1
dlzka = len(cisla)
slovo = ""

for cislo in range(len(cisla)):
    for cislo1 in range(len(cisla)):
        
        cisla = []
        for pismeno1 in nahrada:
            cisla.append(pismeno1)
        
        sucet += int(cisla[i])
        cisla[i]= " "
        
        for cislo2 in cisla:
            
            if j == (dlzka):
                print(j,dlzka)
                break
            
            sucet += int(cisla[j])
            cisla[j] = " "
            j += 1
            
            for pismeno in cisla:
                if cisla[k] == " ":
                    k -= 1
                    pass
                else:
                    sucet1 += int(cisla[k])
                    k -= 1
    
            if sucet > sucet1:
                break
            elif sucet == sucet1:
                slovo = "nasiel"
        
                break
            sucet1 = 0
            k = dlzka -1
            
        sucet = 0   
        k = dlzka -1    
        posuvatel += 1    
        j = posuvatel
        
        if j == dlzka:
            break
        if slovo == "nasiel":
            break
    i += 1
    j = i + 1
    posuvatel = j
    if i == dlzka-1:
        break
    if slovo == "nasiel":
        break
    
print("kokot",slovo)
