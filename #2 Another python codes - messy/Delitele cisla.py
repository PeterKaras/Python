pocet = int(input("Zadajte pocet cisiel, kt chcete zadavat: "))
delitel = int(input("Zadajte cislo, kt chcete najst delitele: "))
cisla = []
vysledok = []
pocet_cisiel = ""
delitel_1 = ""


while pocet != 0:
    cislo = int(input("Zadajte cislo od 0-50: "))
    cisla.append(cislo)
    pocet -= 1

for cislo in cisla:
    if delitel % cislo == 0:
        vysledok.append(cislo)
    pocet_cisiel += str(cislo)
    pocet_cisiel += " "

for cislo in vysledok:
    delitel_1 += str(cislo)
    delitel_1 += " "

dlzka = len(vysledok)

print("Povodne pole:",pocet_cisiel)
print("Pocet delitelov cisla",delitel,":",dlzka)
print("Delitele:",delitel_1)
    
