cisla = [1,2,2,2,4,6,6,7]
ostatok = 0
maxi = 0
pokusy = []
hladat = 0
for cislo in cisla:
    if ostatok == cislo:
        pass
    else:
        cislo1 = cisla.count(cislo)
        if cislo1 > maxi:
            maxi = cislo1
            hladat = cislo

    ostatok = cislo

print(maxi)
for cislo in cisla:
    if cislo == hladat:
        pass
    else:
        if cislo < hladat:
            cislo1 = hladat - cislo
        else:
            cislo1 = cislo - hladat
        pokusy.append(cislo1)
print(pokusy)
