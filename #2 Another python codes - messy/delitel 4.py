cisla = []
slovo = ""
zvysok = 0
cislo1 = 0
pocet = 0
temp = 0

for i in range(1000,9999):
    #print(i)
    cisla = []
    slovo = ""
    k = 0
    j = 0
    temp = 0

    for cislo2 in str(i):
        cisla.append(cislo2)
    #print(cisla)
    
    for cislo2 in cisla:
        #print(cislo2)
        if cislo2 == "9" or cislo2 == "8" or cislo2 == "7":
            #print("KOKOT")
            slovo = "koniec"
            
    for k in range(len(cisla)-1,0,-1):
        for j in range(k):
            if int(cisla[j]) > int(cisla[j+1]):
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
                
    j = 0
    k = 0
    
    #print(cisla)
    for cislo1 in cisla:
        for cislo in cisla:
            if j <= k:
                j += 1
                pass
            else:
                if int(cisla[k]) == int(cisla[j]):
                    #print("SU")
                    slovo = "koniec"
                    break
                else:
                    j += 1
                    continue
        j = 0
        k += 1
    
    if int(i) < 4:
        pass
    else:
        zvysok = int(i) % int(4)
        #print(zvysok,i,"4")
        #print(zvysok)
        if zvysok == 0:
            if slovo == "koniec":
                pass
            else:
                #print(i)
                pocet += 1
        
        else:
            continue
    temp = 0
print(pocet)
