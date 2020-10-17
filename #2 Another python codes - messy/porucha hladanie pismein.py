listy = ['o', 'o', 'o', '.', 'o', '.', 'o', 'o', 'o', '.']
cisla = []
pocet = 0
maxi = 0
k =0
l = 0
hladat = 0
pokusy = []
vysledok = 0

for pismeno in listy:
    if pismeno == "o":
        pocet += 1
    else:
        cisla.append(pocet)
        pocet = 0

print(cisla)
for k in range(len(cisla)-1,0,-1):
    for l in range(k):
        if cisla[l]>cisla[l+1]:
            temp = cisla[l]
            cisla[l] = cisla[l+1]
            cisla[l+1] = temp

print(cisla)
k = 0
for cislo in listy:
    cislo1 = cisla.count(k)
    if cislo1 > maxi:
        maxi = cislo1
        hladat = k
    print(k)
    k += 1

print(maxi, hladat)
for cislo in cisla:
    if cislo == hladat:
        pass
    else:
        if cislo < hladat:
            cislo1 = hladat - cislo
        else:
            cislo1 = cislo - hladat
        pokusy.append(cislo1)

for cislo in pokusy:
    vysledok += cislo

print(vysledok)
