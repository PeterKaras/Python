def kontrola(cisla,pocet,dopocet=0):
    for cislo in cisla:
        if cislo.isdigit() == True:
            pass
        elif cislo.replace('-', '', 1).isdigit() == True:
            pass
        else:
            return "Ne"
        dopocet += 1
    if dopocet == int(pocet):
        return "ok"
    else:
        return "Ne"

def hlavny_cyklus(cisla,pocet,sucet=1,maxi=0,j=0):
    #cisla = zoradenie(cisla)
    for i in range(int(pocet)):
        sucet *= int(cisla[i])
        if sucet > maxi:
            maxi = sucet
        for j in range(i+1,pocet):
            sucet *= int(cisla[j])
            if sucet > maxi:
                maxi = sucet
            else:
                pass
        sucet = 1
    return maxi

"""def zoradenie(cisla):#mozno toto bude treba ak to nema ist za sebou 
    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if int(cisla[j]) > int(cisla[j+1]):
                temp = cisla[j]
                cisla[j] = cisla[j+1]
                cisla[j+1] = temp
    return cisla"""

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet cisiel: ").strip()
        if pocet.isdigit() == True:
            cisla = input("Zadajte vase cisla: ").split()
            znak = kontrola(cisla,pocet)
            print(znak)
            if znak == "ok":
                print(hlavny_cyklus(cisla,int(pocet)))
            else:
                print("Nezadali ste cisla!")
                continue
        else:
            print("Nezadali ste cislo!")
            continue
        
        cyklus = int(cyklus)-1
