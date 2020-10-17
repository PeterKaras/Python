pocet = 0

for cislo in range(1000):
    if cislo % 7 == 0:
        print(cislo)
        pocet += 1
    else:
        pass


print("7",pocet)

pocet = 0

for cislo in range(1000):
    if cislo % 13 != 0:
        #print(cislo)
        pocet += 1
    else:
        pass

print("13",pocet)

pocet = 0

for cislo in range(1000):
    if cislo % 3 == 0 and cislo % 4 == 0:
        #print(cislo)
        pocet += 1
    else:
        pass

print("3 a 4",pocet)

pocet = 0

for cislo in range(1000):
    if cislo % 3 == 0 or cislo % 4 == 0:
        #print(cislo)
        pocet += 1
    else:
        pass

print("3 alebo 4",pocet)
