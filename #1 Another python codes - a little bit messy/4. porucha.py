def nacitanie(pocet,kontrola=""):
    slova = []
    for i in range(pocet):
        slovo = input("Zadajte slovo: ").strip()
        porovnanie = zistenie(slovo)
        if kontrola == porovnanie or kontrola == "":
            slovo = rozdelenie(slovo)
            slova.append(slovo)
            kontrola = porovnanie
        else:
            return "-1"
    return slova,porovnanie

def zistenie(slova,slovo = "", zostatok = ""):
    for pismeno in slova:
        if zostatok == pismeno:
            pass
        else:
            slovo += str(pismeno)            
        zostatok = pismeno
    return slovo

def rozdelenie(slovo):
    slova1 = []
    for pismeno in slovo:
        slova1.append(pismeno)
    return slova1

def zistenie(slova,slovo = "", zostatok = ""):
    for pismeno in slova:
        if zostatok == pismeno:
            pass
        else:
            slovo += str(pismeno)            
        zostatok = pismeno
    return slovo

def hlavny_cyklus(slova,porov,zostatok = "",new = [],pocet1 = 0):
    new = []
    for k in range(len(porov)):
        for i in range(len(slova)):
            for j in range(len(slova[i])):
                if slova[i][j] == porov[k]:
                    zostatok += slova[i][j]
                else:
                    pass
            slovo = list(zostatok)
            new.append(slovo)
            zostatok = ""
        prepocty = pocitanie(new)
        pocet1 += koniec(prepocty)
        new = []
    return pocet1

def pocitanie(new):
    pocet=[]
    for cell in new:
        pocet.append(len(cell))
    return pocet

def koniec(prepocty,pocet = 0):

    prepocty = zoradenie(prepocty)
    index1 = len(prepocty)//2
    for cislo in prepocty:
        if cislo <= index1:
            pocet += (prepocty[index1] - cislo)
        else:
            pocet += (cislo - prepocty[index1])
    return pocet

def zoradenie(cisla):
    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if cisla[j] > cisla[j+1]:
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
    return cisla
        
cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet slov: ").strip()
        if pocet.isdigit() == True:
            slova = nacitanie(int(pocet))
            if slova != "-1":
                print(hlavny_cyklus(slova[0],slova[1]))
            else:
                print("-1")
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1 
else:
    print("Nezadali ste cislo!")
