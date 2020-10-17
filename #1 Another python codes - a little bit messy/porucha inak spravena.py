def nacitanie(pocet,slova = [],kontrola = ""):
    slova = []
    while pocet != 0:
        slovo = input("Zadajte slovo: ").strip()
        porovnanie = zistenie(slovo)
        if kontrola == "":
            kontrola = porovnanie
            slovo = rozdelenie(slovo)
            slova.append(slovo)
        elif kontrola == porovnanie:
            slovo = rozdelenie(slovo)
            slova.append(slovo)
        else:
            return "-1"
        pocet -= 1
    print(slova)
    return slova

def rozdelenie(slovo):
    slova = []
    for pismeno in slovo:
        slova.append(pismeno)
    return slova

def zistenie(slova,slovo = "", zostatok = ""):
    for pismeno in slova:
        if zostatok == pismeno:
            pass
        else:
            slovo += str(pismeno)            
        zostatok = pismeno
    return slovo

def triedenie(slova,i,j=0,zostatok="",ok="ok",nove="",spajanie=""):
    for pismeno in slova[i]:
        zostatok = pismeno
        if slova[i][j] == zostatok and ok == "ok":
            spajanie += str(slova[i][j])
            if j == len(slova[i])-1:
                if slova[i][j] != zostatok:
                    ok = "Ne"
                    break
            elif slova[i][j+1] != zostatok:
                ok = "Ne"
        else:
            nove += str(pismeno)       
        j += 1
    return spajanie,nove

def hlavny_cyklus(slova,i=0,pocet=0):
    new = []
    while True:
        pole = triedenie(slova,i)
        pole1 = rozdelenie(pole[0])
        new.append(pole1)
        nove_slova = rozdelenie(pole[1])
        slova[i] = nove_slova
        i += 1
        if i == len(slova):
            pocet += int(pocitanie(new))
            new = []
            i = 0
        if slova[-1] == []:
            break
    return pocet

def pocitanie(new,maxi = 0,ostatok = "",vysledok = 0,hladat = 0):
    cisla = []
    for slovo in new:
        pocet = len(slovo)
        cisla.append(pocet)
        
    cisla = zoradenie(cisla)
    for cislo in cisla:
        if ostatok == cislo:
            pass
        else:
            cislo1 = cisla.count(cislo)
            if cislo1 > maxi:
                maxi = cislo1
                hladat = cislo
        ostatok = cislo
    print(cisla)   
    for cislo in cisla:
        if cislo == hladat:
            pass
        else:
            if cislo < hladat:
                cislo1 = hladat - cislo
            else:
                cislo1 = cislo - hladat
            vysledok += cislo1
    return vysledok

def zoradenie(pocty):
    for i in range(len(pocty)-1,0,-1):
        for j in range(i):
            if pocty[j] > pocty[j+1]:
                temp = pocty[j]
                pocty[j] = pocty[j+1]
                pocty[j+1] = temp
    return pocty

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet slov: ").strip()
        if pocet.isdigit() == True:
            slova = nacitanie(int(pocet))
            if slova != "-1":
                print(hlavny_cyklus(slova))
            else:
                pass
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo!")
