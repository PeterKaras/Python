def nacitanie(pocet):
    listy=[]
    for i in range(2):
        znaky = input("Zadajte vase znaky: ").strip()
        znak = kontrola(znaky,int(pocet))
        if znak == "ok":
            listy.append(list(znaky))
        else:
            return "Ne"
    return listy 

def kontrola(znaky,pocet,dopocet=0):
    for znak in znaky:
        if znak == "." or znak == "#":
            pass
        else:
            return "Ne"
        dopocet += 1
    if dopocet == int(pocet):
        return "ok"
    else:
        return "Ne"

def hlavny_cyklus(znaky,pocet,i=0,j=0,zaciatok=0,porov=0,pocet1=0):
    indexy = indexovanie(znaky)
    if indexy == "ne":
        return "Prepracovať"
    else:
        indexy = zoradenie(indexy)
        znaky[0].insert(len(znaky[0]),".")
        znaky[1].insert(len(znaky[1]),".")
        j = indexy[i+1]
        for k in range(len(indexy)):
            for m in range(2):
                for p in range(zaciatok,j+1):
                    if znaky[m][p] == "#":
                        pocet1 += 1
                    else:
                        pass
                if m == 1:
                    if porov%2 != 0 and pocet1%2 != 0:
                        return "Prepracovat"
                    else:
                        pass
                else:
                    porov=pocet1
                    pocet1 = 0
            pocet1 = 0
            i += 1
            if i == len(indexy)-1:
                break
            zaciatok = indexy[i]
            j = indexy[i+1]
    return "V poriadku"       

def indexovanie(znaky,indexy=[],slovo="",i=0):
    indexy = []
    for j in range(len(znaky)):
        for znak in znaky[j]:
            if znak == ".":
                if i in indexy:
                    slovo = "Ne"
                else:
                    if slovo == "Ne":
                        if znak == "#":
                            return "ne"
                    else:
                        indexy.append(i)
            else:
                if slovo == "Ne":
                    return "ne"
            i += 1
        i = 0
    if indexy[0] == 0:
        pass
    else:
        indexy.insert(0,0)
    indexy.append(len(znaky[0]))
    return indexy

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
        pocet = input("Zadajte pocet znak na zadavanie: ").strip()
        if pocet.isdigit() == True:
            znaky = nacitanie(pocet)
            if znaky != "Ne":
                print(hlavny_cyklus(znaky,pocet))
            else:
                print("Nezadali ste spravne znaky!")
                continue 
        else:
            print("Nezadali ste cislo!")
            continue 
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
