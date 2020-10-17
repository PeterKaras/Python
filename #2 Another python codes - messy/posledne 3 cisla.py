cislo = input("Zadajte cislo: ")
cisla = []
vysledok = ""

for i in cislo:
    cisla.append(i)
    
dlzka = len(cisla)
dlzka1 = dlzka - 3

for i in cisla[dlzka1:dlzka]:
    vysledok += i
    vysledok += ", "
    
print(vysledok)
