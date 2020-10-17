cislo = int(input("Zadajte cislo: "))
dlzka = len(str(cislo))
print(dlzka)

if dlzka == 3:
    for i in range(2,cislo):
        if (cislo % i) == 0:
            print(cislo,"nie je zaujimave!")
            break
    else:
        print(cislo,"je pre nas zaujimave")
else:
    print("cislo nie je zaujimave pre nas!")
