cisla = [1,4,6]
i = 0
dlzka = len(cisla)-1
print(dlzka)
for cislo1 in range(2):
    for cislo in cisla:
        sucet = (cisla[i+1] - cisla[i])-1
        print(sucet)
        i += 1
        if i == dlzka:
            break
    i = 0
