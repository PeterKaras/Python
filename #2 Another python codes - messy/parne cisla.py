pocet = int(input("Zadajte kolko cisiel chcete zadavat: "))
cisla = []
vysledok = []
pocet_cisiel = ""
parne = ""
while pocet != 0:
    cislo = int(input("Zadajte cislo od 0-50: "))
    cisla.append(cislo)
    pocet -= 1

for cislo in cisla:
    if cislo % 2 == 0:
        vysledok.append(cislo)

dlzka = len(vysledok)

for cislo in cisla:
    pocet_cisiel += str(cislo)
    pocet_cisiel += " "


for cislo in vysledok:
    parne += str(cislo)
    parne += " "

print("Cisla su:",pocet_cisiel)
print("Pocet parnych cisiel:",dlzka)
print("Parne cisla su:",parne)
