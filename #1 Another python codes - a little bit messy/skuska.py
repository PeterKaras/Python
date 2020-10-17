zoradenie = [0,1,2,3,6]
sucet =0
s = 0
medzi = []

for i in range(len(zoradenie)):
    sucet += zoradenie[i]
    medzi.append(i)
    for j in range(i+1,len(zoradenie)):
        sucet += zoradenie[j]
        #print("j",cisla[j])
        medzi.append(j)
        print(sucet)
        #print(medzi)
        for k in range(len(zoradenie)):
            if k in medzi:
                 pass
            else:
                s += zoradenie[k]
                #print(cisla[k])
        if s == sucet:
            print("kokot")
            break
        #print(cisla[i],cisla[j],cisla[k])
        print(s)
        s=0

    if s == sucet:
        print("jj")
        break
    medzi = []
    sucet = 0  
