def kontrola(cisla,pocet,dopocet = 0):
    for cislo in cisla:
        if cislo.isdigit() == True:
            pass
        elif cislo.upper() == "COUNT" or cislo.upper() == "UPDATE":
            pass
        else:
            return "Ne"
        dopocet += 1
    if dopocet == pocet:
        return "ok"
    else:
        return "NE"

def hlavny_cyklus(cisla,procesy,delitel):
    while int(procesy) != 0:
        prikaz = input("Zadajte vas prikaz: ").split()
        znak = kontrola(prikaz,pocet = 3)
        if znak == "ok":
            if prikaz[0].upper() == "COUNT":
                pocet = count(cisla,delitel,prikaz)
                print(pocet)
            elif prikaz[0].upper() == "UPDATE":
                cisla = update(cisla,prikaz)
            else:
                print("Nezadali ste spravny prikaz!")
                procesy = int(procesy) + 1
        else:
            print("Nezadali ste spravne symboly!")
            continue
        procesy = int(procesy) - 1

def count(cisla,delitel,prikaz,pocet=0,j=0,vysledok=0):
    j = int(prikaz[1])
    for i in range(int(prikaz[2])-int(prikaz[1])):
        for cislo in range(j,int(prikaz[2])):
            pocet += int(cisla[cislo])
            if (pocet%delitel)==0:
                   vysledok += 1
        pocet = 0
        j += 1
    return vysledok

def update(cisla,prikaz):
    cislo = int(prikaz[1])
    cisla[cislo] = prikaz[2]
    return cisla
        
cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        zaciatok = input("Zadajte zaciatok: ").split()
        znak = kontrola(zaciatok,pocet = 2)
        if znak == "ok":
            cisla = input("Zadajte cisla: ").split()
            znak = kontrola(cisla,pocet = int(zaciatok[0]))
            if znak == "ok":
                procesy = input("Zadajte cislo: ").strip()
                if procesy.isdigit() == True:
                    hlavny_cyklus(cisla,procesy,int(zaciatok[1]))
                else:
                    continue
            else:
                continue 
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1 
