cisla = ['1', '0', '1', '0', '0']
indexy = [0,2]
i = 0
pocet = 0
for cislo in cisla:
    if cislo == "1":
        indexy.append(i)
    else:
        pass
    i += 1
    
#print(indexy)

zostatok = [1,2]

#print(zostatok)
for cislo in zostatok:
    print(cislo)
    if cislo in indexy:
         pass
    else:
        pocet += 1


print(pocet)
