pocet_inte = int(input("Zadajte pocet: "))
i = 0
k = 0
cislo2 = ""
cisla = []
cisla1 = []
pocet = 0
x = 0
cislo3 = 0
prazdna = 0
dobre = 0
vysledok = 0
cislo4 = 0
sucet = 0
sucet1 = 0
p = 0
l = 0
cislo5 = 0

print(pocet)
while pocet_inte != 0:
    cislo= int(input("Zaciatok: "))
    cislo1 = int(input("koniec: "))
    for i in range(cislo,cislo1+1):
        #print(i)
        cislo2 = str(i)
        dlzka = len(cislo2)
        if dlzka == 1:
            continue
        elif dlzka == 2:
            for pismeno in str(cislo2):
                cisla.append(pismeno)
                cisla1.append(pismeno)
                
            if int(cisla[0]) == int(cisla1[1]):
                pocet += 1
            print(cisla) 
        elif dlzka == 3:
            for pismeno in str(cislo2):
                cisla.append(pismeno)
                cisla1.append(pismeno)
                
            for j in range(len(cisla)-1,0,-1):
                for k in range(j):
                    if cisla[k] > cisla[k+1]:
                        temp = cisla[k]
                        cisla[k] = cisla[k+1]
                        cisla[k+1] = temp
            
            print(cisla)
            vysledok = int(cisla[0]) + int(cisla[1])
            #print(vysledok,cisla[2])
            if vysledok == int(cisla[2]):
    
                pocet += 1
                #print(pocet,i)
                cisla1 = []
                cisla = []
            else:
                cisla1 = []
                cisla = []
                continue
            
        elif dlzka == 4 or dlzka == 5 or dlzka == 6:
            for pismeno in str(cislo2):
                cisla.append(pismeno)
                cisla1.append(pismeno)
                
            for j in range(len(cisla)-1,0,-1):
                for k in range(j):
                    if cisla[k] > cisla[k+1]:
                        temp = cisla[k]
                        cisla[k] = cisla[k+1]
                        cisla[k+1] = temp

            for j in range(len(cisla1)-1,0,-1):
                for k in range(j):
                    if cisla1[k] > cisla1[k+1]:
                        temp = cisla1[k]
                        cisla1[k] = cisla1[k+1]
                        cisla1[k+1] = temp
                        
            #print(cisla)
            dlzka = len(cisla)
            for cislo in cisla:
                sucet += int(cisla[p])    
                #print(sucet)
                p += 1
                if p == (dlzka-1):
                    break
                
            if sucet == int(cisla[dlzka-1]):
                pocet += 1

            for j in cisla:
                for m in cisla:
                    if sucet == int(cisla[dlzka-1]):
                        break
                    
                    if k <= x:
                        #print("BUH")
                        pass
                    if x < k:
                        #print(cisla)
                        cislo3 = int(cisla[x])
                        cislo4 = int(cisla[k])
                        vysledok = int(cisla[x]) + int(cisla[k])
                        #print(vysledok)
                        cisla[x] = " "
                        cisla[k] = " "
                        
                        for pismeno in cisla:
                            if pismeno == " ":
                                pass
                            else:
                                prazdna += int(pismeno)
                                
                        dobre = prazdna
                        if vysledok == dobre:
                            #print("breakk")
                            pocet += 1
                            break
                        #print("p",prazdna)
                        #print(cisla)
                        cisla[x] = str(cislo3)
                        cisla[k] = str(cislo4)
                        
                        cisla = []
                        for pismeno in cisla1:
                            cisla.append(str(pismeno))
                            
                        prazdna = 0
                        if vysledok == dobre:
                            #print("breakk")
                            pocet += 1
                            break
                        
                       
                    k += 1
                if vysledok == dobre:
                    break
                    
                #print("x",x)
                k = 0
                x += 1
                    
        if dlzka == 7 or dlzka == 8:
            
            for pismeno in str(cislo2):
                cisla.append(pismeno)
                cisla1.append(pismeno)
                
            for j in range(len(cisla)-1,0,-1):
                for k in range(j):
                    if cisla[k] > cisla[k+1]:
                        temp = cisla[k]
                        cisla[k] = cisla[k+1]
                        cisla[k+1] = temp

            for j in range(len(cisla1)-1,0,-1):
                for k in range(j):
                    if cisla1[k] > cisla1[k+1]:
                        temp = cisla1[k]
                        cisla1[k] = cisla1[k+1]
                        cisla1[k+1] = temp
                        
            #print(cisla)
            dlzka = len(cisla)
            for cislo in cisla:
                sucet += int(cisla[p])    
                #print(sucet)
                p += 1
                if p == (dlzka-1):
                    break
                
            if sucet == int(cisla[dlzka-1]):
                pocet += 1

            for j in cisla:
                for m in cisla:
                    if sucet == int(cisla[dlzka-1]):
                        break
                    if k <= x:
                        #print("BUH")
                        pass
                    if l <= x:
                        pass
                    if k < l:
                        #print(cisla)
                        cislo3 = int(cisla[x])
                        cislo4 = int(cisla[k])
                        cislo5 = int(cisla[l])
                        vysledok = int(cisla[x]) + int(cisla[k]) + int(cisla[l])
                        #print(vysledok)
                        cisla[x] = " "
                        cisla[k] = " "
                        cisla[l] = " "
                        
                        for pismeno in cisla:
                            if pismeno == " ":
                                pass
                            else:
                                prazdna += int(pismeno)
                                
                        dobre = prazdna
                        #print("p",prazdna)
                        if vysledok == dobre:
                            #print("breakk")
                            pocet += 1
                            break
                        #print("p",prazdna)
                        #print(cisla)
                        cisla[x] = str(cislo3)
                        cisla[k] = str(cislo4)
                        cisla[l] = str(cislo5)
                        
                        cisla = []
                        for pismeno in cisla1:
                            cisla.append(str(pismeno))
                            
                        prazdna = 0
                        if vysledok == dobre:
                            #print("breakk")
                            pocet += 1
                            break

                    l += 1

                if vysledok == dobre:
                    #print(i)
                    break


                l = 0
                x += 1
                k = x + 1
                
        
        dobre = 0
        prazdna = 0
        k = 0
        x = 0
        l = 0
        j = 0
        p = 0
        m = 0
        sucet1 = 0 
        sucet = 0
        vysledok = 0
        cisla = []
        cisla1 = []
        dlzka = 0
        #print(pocet,i)
        i +=1
        
    cisla = []
    cisla1 = []
    k = 0
    x = 0
    j = 0
    prazdna = 0
    vysledok = 0
    
    print(pocet)
    pocet = 0
    pocet_inte -= 1 
