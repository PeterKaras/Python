pocet = int(input("Zadajte pocet cisiel, kt chcete zadavat: "))
pocet1 = pocet
cisla1 = []
cisla2 = []
vysledok = 0
celkovy = 0
i = 0


while pocet != 0:
    cislo = float(input("Zadajte cisla pre A vektor: "))
    cisla1.append(cislo)
    pocet -= 1

while pocet1 != 0:
    cislo = float(input("Zadajte cisla pre B vektor: "))
    cisla2.append(cislo)
    pocet1 -= 1

while True:
    vysledok = cisla1[i] * cisla2[i]
    celkovy += vysledok
    i += 1
    if i == pocet:
        break
    print(celkovy)
