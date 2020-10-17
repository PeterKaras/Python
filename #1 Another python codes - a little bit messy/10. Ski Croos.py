def kontrola(cisla,pocet,dopocet = 0):
    for cislo in cisla:
        if cislo.isdigit() == True:
            pass
        else:
            return "Ne"
        dopocet += 1
    if dopocet == pocet:
        return "ok"
    else:
        return "Ne"

def hlavny_cyklus(cisla,string = ""):
    prve_cislo = cisla[0]*int(cisla[1])
    druhe_cislo = cisla[2]*int(cisla[3])
    if len(prve_cislo) > len(druhe_cislo):
        return "Vacsie"
    elif len(prve_cislo) < len(druhe_cislo):
        return "Mensie"
    else:
        return "Rovne"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        cisla = input("Zadajte cisla: ").split()
        znak = kontrola(cisla,pocet = 4)
        if znak == "ok":
            print(hlavny_cyklus(cisla))
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo!")
