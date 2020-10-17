cisla =  ['3', '4', '5', '6']
dlzka = len(cisla)
pocet = 0
parne = 0
i = 0
j = 0
slovo = ""
slovo1 = ""
for cislo in range(int(cisla[-1])+1):
    if j < int(cisla[0]):
        j += 1
        pass
    else:
        for cislo in cisla:
            if j == int(cislo):
                slovo1 = ""
                print("k",j,int(cislo))
                break
            else:
                slovo1 = "missing"
                print(j,cislo)
                pocet += 1
        j += 1
    if slovo1 == "missing":
        break
    pocet = 0
    
pocet = 0
i = 0
j = 0
print(slovo1)
for cislo in cisla:
    if slovo1 == "missing":
        cislo1 = int(cisla[i]) + 1
        if cislo1 != int(cisla[i+1]):
            slovo = "koniec"
            break
        else:
            pocet += 1
        cislo1 = 0
        i += 1
        if i == (dlzka):
            break

    else:
        cislo1 = int(cisla[i]) + 1
        if cislo1 != int(cisla[i+1]):
            slovo = "koniec"
            break
        else:
            pocet += 1
        cislo1 = 0
        i += 2
        if i == (dlzka):
            break





i = 0


print(pocet)
