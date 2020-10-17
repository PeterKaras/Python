def nacitanie(vzor,hlavne_cisla=[]):
    odpocet = int(vzor[0])
    while odpocet != 0:
        cisla = input("Zadajte cisla: ").split()
        znak = kontrola(cisla,pocet = int(vzor[1]))
        if znak == "ok":
            hlavne_cisla.append(list(cisla))
        else:
            continue
        odpocet -= 1
    hlavny_cyklus(hlavne_cisla,vzor)
    return 0
    
def kontrola(cisla,pocet,pocitadlo = 0):
    for cislo in cisla:
        if cislo.isdigit() == True:
            pocitadlo += 1
        elif cislo.replace('-', '', 1).isdigit() == True:
            pocitadlo += 1
        else:
            return "Ne"
        
    if pocitadlo != pocet:
        return "Ne"
    else:
        return "ok"

def hlavny_cyklus(cisla,vzor,hranica=1,maxi=0,zaciatok=0,riadok=0,dlzka=1,pocet=0):
    while True:
        for indexy in range(riadok,dlzka):
            for cislo in range(zaciatok,hranica):
                pocet += int(cisla[indexy][cislo])
        if pocet > maxi:
            maxi = pocet
            pocet = 0
        else:
            pocet = 0
        hranica += 1
        dlzka += 1
        if dlzka == len(cisla)+1 or hranica == len(cisla[0])+1:
            zaciatok += 1
            hranica = (zaciatok +1)
            dlzka = riadok + 1
            if zaciatok == len(cisla[0]):
                riadok += 1
                zaciatok = 0
                hranica = 0
            if riadok == len(cisla):
                break

    print(maxi)




cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        vzor = input("Zadajte pocetnost: ").split(" ")
        znak = kontrola(vzor,pocet=2)
        if znak == "ok":
            nacitanie(vzor)
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1
    
else:
    priont("Nezadali ste cislo!")
