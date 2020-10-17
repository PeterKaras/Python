def kontrola(prikazy,pocet,dopocet=0):
    sirka= []
    dlzka= []
    for pismeno in prikazy:
        if pismeno.isdigit() == True:
            pass
        elif pismeno.upper() == "L" or pismeno.upper() == "P":
            sirka.append(pismeno)
        elif pismeno.upper() == "H" or pismeno.upper() == "D":
            dlzka.append(pismeno)
        else:
            return "Ne"
        dopocet += 1
    if dopocet == pocet:
        return "ok",sirka,dlzka
    else:
        return "Ne"

def hlavny_cyklus(sirka,dlzka,rozmedzie,zostatok="",s=0,d=0):
    zostatok = sirka[0]
    for pismeno in sirka:
        if pismeno == zostatok:
            s +=1
        else:
            s -= 1
        if s < 0:
            s *= -1
        if s == int(rozmedzie[1]):
            return "mantinel"
        else:
            pass
    zostatok = dlzka[0]
    for pismeno in dlzka:
        if pismeno == zostatok:
            d +=1
        else:
            d -= 1
        if d < 0:
            d *= -1
        if d == int(rozmedzie[0]):
            return "mantinel"
        else:
            pass        
    return "v poriadku"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        rozmedzie = input("Zadajte rozmedzie klziska: ").split()
        znak = kontrola(rozmedzie,pocet=2)
        if znak[0] == "ok":
            prikazy = input("Zadajte vase prikazy: ")
            znak = kontrola(prikazy,pocet=len(prikazy))
            if znak[0] == "ok":
                print(hlavny_cyklus(znak[1],znak[2],rozmedzie))
            else:
                print("Nezadali ste spravne znaky!")
                continue
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
