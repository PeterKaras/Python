def nacitanie():
    cisla = input("Zadajte cisla: ").strip()
    znak = kontrola(cisla)
    if znak == "Ne":
        return "-1"
    else:
        zoradenie(znak)

def kontrola(cisla,nove = []):
    for cislo in cisla:
        if cislo == "1" or cislo == "0":
            nove.append(cislo)
            pass
        else:
            return "Ne"
    return nove

def zoradenie(cisla,pocet = 0,zostatok = [],indexy = []):
    zostatok = indexovanie(cisla,zostatok)
    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if int(cisla[j]) > int(cisla[j+1]):
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
                pocet += 1         
        indexy = indexovanie(cisla)
        if indexy == zostatok:
            pass
        else:
            pocet += int(zistenie(indexy,zostatok))
        zostatok = indexy
    return 0

def indexovanie(cisla,indexy1 = [],i = 0):
    indexy1 = []
    for cislo in cisla:
        if cislo == "1":
            indexy1.append(i)
        else:
            pass
        i += 1                
    return indexy1

def zistenie(indexy2,zostatok,pocet=0):
    for cislo in zostatok:
        if cislo in indexy2:
            pass
        else:
            pocet += 1
    return pocet
                
cyklus = input("Zadajte pocet cyklus: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pole = nacitanie()
        if pole == "-1":
            continue
        else:
            cyklus = int(cyklus) -1
else:
    print("Nezadali ste cislo!")
