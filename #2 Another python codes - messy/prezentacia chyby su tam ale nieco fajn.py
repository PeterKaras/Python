cisla = ["0","0","1","1","1","0","1","0","0","0","1","1","0","1","0","1"]
vysledok = ['0','0','0','0', '0', '0', '0','0','1','1','1','1','1','1','1','1']
vysledne = []
predosle = 0
i= 0
k = 0
pocet = 0
docasne = []
pocet_indexov = 0
jednotky = 0

for pismeno in cisla:
    docasne.append(pismeno)
    
print(docasne)
i = 0
j = 0
index = []
dlzka = len(cisla)
vysledne = []
zadok = []
predok = []

for pismeno in cisla:
    if cisla[j] == "1":
        index.append(str(j))
    j += 1

j = 0
i = 0

dlzka = len(index)
print("DLZKA",dlzka)
for pismeno1 in cisla:
    for pismeno in cisla:
        #print(index)   
        j = 0
        
        #for pismeno in docasne:
            #cisla.append(pismeno)
        #print(cisla)
        
        if i == dlzka:
            break   
        #print(i)
        index1 = int(index[i])
        print("i",index[i])
        i += 1
    
        if i == (dlzka):
            break
        else:
            index2 = int(index[i])
            #print("i2",index2)
            #pocet_indexov += 1
    
        for pismeno in cisla:
            if index1 == 0:
                pass
            else:
                #print("Buh")
                predok.append(cisla[j])
                cisla[j] = " "
                j += 1
                if j == int(index1):
                    break
    
        j = 0
        #print(j)
        #print("P",predok)
        
        for pismeno in cisla:
            if j < int(index2+1):
                j += 1
                pass
            else:
                zadok.append(cisla[j])
                cisla[j] = " "
                
                j += 1
                
        #print("z",zadok)     
        for pismeno in cisla:
            if pismeno == " ":
                pass
            else:
                vysledne.append(pismeno)
            
        #print(cisla)    
        #print(vysledne)
        
        j = 0
        for i in range(len(vysledne)-1,0,-1):
            for j in range(i):
                if int(vysledne[j]) > int(vysledne[j+1]):
                    pocet += 1
                    temp = vysledne[j]
                    vysledne[j] = vysledne[j+1]
                    vysledne[j+1] = temp

        if pocet != 0:
            pocet += 1
        #print(cisla)
        #print(vysledne)
        cisla = []
        for pismeno3 in predok:
            cisla.append(pismeno3)
        for pismeno3 in vysledne:
            cisla.append(pismeno3)
        for pismeno3 in zadok:
            cisla.append(pismeno3)
        #print(cisla)
        #print("k",pocet)
        j = 0
        zadok = []
        predok = []
        vysledne = []
        #i += 1
        if cisla == vysledok:
            break
        #if pocet_indexov == (dlzka-1):
            #break
    index = []
    for pismeno in cisla:
        if cisla[j] == "1":
            index.append(str(j))
        j += 1
    if cisla == vysledok:
            break
    i = 0
    j = 0

j = 0
j = len(docasne)-1
for cislo3 in cisla:
    if docasne[j] == "1":
        jednotky += 1
    else:
        break
    j -= 1
print(jednotky)
jednotky1 = cisla.count("1")-jednotky
print(pocet)
