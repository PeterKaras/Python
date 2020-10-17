pocet = int(input("Zadajte pocet cisiel, kt chcete zadavat: "))
nasobok = int(input("Zadajte nasobok kt chcete hladat: "))
cisla = []
vysledok = []
pocet_cisiel = ""
nasobok1 = ""

while pocet != 0:
    cislo = int(input("Zadajte cislo od 0-50: "))
    cisla.append(cislo)
    pocet -= 1

for cislo in cisla:
    if cislo % nasobok == 0:
        vysledok.append(cislo)

for cislo in cisla:
    pocet_cisiel += str(cislo)
    pocet_cisiel += " "

dlzka = len(vysledok)

for cislo in vysledok:
    nasobok1 += str(cislo)
    nasobok1 += " "

print("Cisla, kt ste zadali:",pocet_cisiel)
print("Pocet cisiel kt su nasobkom cisla",nasobok,":",dlzka)
print("Cisla, kt su nasobkom cisla",nasobok,"su:",nasobok1)
    
