def kontrola(cisla,pocet,dopocet=0):
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

def hlavny_cyklus(cisla,pocet,pokusy = 0):
    for i in range(1,int(pocet)+1):
        indexy = cisla.index(str(i))
        if (int(i)-1) == int(indexy):
            pass
        else:
            temp = cisla[indexy]
            cisla[indexy] = cisla[int(i)-1]
            cisla[int(i)-1] = temp
            pokusy += 1 
    return pokusy

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet cisiel: ").strip()
        if pocet.isdigit() == True:
            cisla = input("Zadajte cisla: ").split()
            znak = kontrola(cisla,int(pocet))
            if znak == "ok":
                print(hlavny_cyklus(cisla,pocet))
            else:
                print("Nezadali ste cisla!")
                continue
        else:
            print("Nezadali ste cisla!")
            continue
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")


