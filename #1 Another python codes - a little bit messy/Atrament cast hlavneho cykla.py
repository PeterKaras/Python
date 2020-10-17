cisla = [['-5', '-9', '2', '-4', '-7', '7', '-6'],
         ['-5', '-8', '2', '-4', '-7', '7', '-6'],
         ['-5', '-7', '2', '-4', '-7', '7', '-6']]

#print(len(cisla))
hranica = 1
maxi = 0
zaciatok = 0
riadok = 0
dlzka = 1
pomocna = 1
pocet = 0
"""while True:
    for cislo1 in range(len(
    for cislo in range(len(cisla[0])):
        print(cislo)"""







while True:
    for indexy in range(riadok,dlzka):
        for cislo in range(zaciatok,hranica):
            pocet += int(cisla[indexy][cislo])
            print(pocet)
            print(cisla[indexy][cislo])
            #print("CISLA",indexy,cislo)
    print("__________________________")
    if pocet > maxi:
        maxi = pocet
        pocet = 0
    else:
        pocet = 0
    hranica += 1
    dlzka += 1
    if dlzka == len(cisla)+1 or hranica == len(cisla[0])+1:
        zaciatok += 1
        #print("CISLA",zaciatok)
        hranica = (zaciatok +1)
        #print("CISLA",hranica)
        #print("CISLA",zaciatok)
        dlzka = riadok + 1
        print("-----")
        if zaciatok == len(cisla[0]):
            riadok += 1
            zaciatok = 0
            hranica = 0
        if riadok == len(cisla):
            break


print(maxi)










"""for k in range(3):
    for cislo in range(i,hranica):
        #print(i,hranica)
        for cislo1 in range(j,hranica):
            print(cislo1)

    hranica += 1
    if cislo == hranica:
        i += 1
        j = i
        hranica 
    
    print("-----------------")"""
