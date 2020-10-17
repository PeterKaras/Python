index3 = ['0', '1', '2', '4', '5', '6']
j = 0
k = 0
vysledok1 = 0
pocet = 0

dlzka1 = len(index3)
print(index3[-1])
for znak in range(int(index3[-1])):
    if j < int(index3[0]):
        j += 1
        pass
    else:
        for cislo in index3:
            if j == int(cislo):
                print(j,int(cislo))
                break
            else:
                print(j,cislo)
                pocet += 1
        j += 1
        
    if pocet == dlzka1:
        vysledok1 += 1
    pocet = 0
    j
print(vysledok1)
