cislo = 1
cislo1 = 1
scitanie = 0
vysledok = 0

while True:
    vysledok = cislo**2
    scitanie += vysledok
    cislo += 1
    print(vysledok,cislo)
    if cislo > 99:
        break
print("---------")
print(scitanie)
print("---------")

while True:
    vysledok += cislo1
    cislo1 += 1
    print(vysledok, cislo1)
    if cislo1 > 99:
        scitanie1 = vysledok**2
        break
print("---------")
print(scitanie1)
print("---------")

vysledok = 0
vysledok = scitanie1 - scitanie
print(vysledok)
