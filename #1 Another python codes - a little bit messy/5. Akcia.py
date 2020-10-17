def nacitanie(pocet,dni=[]):
    for i in range(int(pocet)):
        cisla = input("Zadajte cisla: ").split(" ")
        
        znak = kontrola(cisla)
        if znak == "ok":
            dni = pridavanie(cisla,dni)
        else:
            return "-1"
    dni = zoradenie(dni)
    return dni

def kontrola(cisla):
    for cislo in cisla:
        if cislo.isdigit() == True:
            pass
        else:
            return "Ne"
    return "ok"

def pridavanie(cisla,dni):
    for cislo in cisla:
        if int(cislo) == 0 or int(cislo) in dni:
            pass
        else:
            dni.append(int(cislo))
    return dni

def zoradenie(dni):
    for i in range(len(dni)-1,0,-1):
        for j in range(i):
            if dni[j] > dni[j+1]:
                temp = dni[j]
                dni[j] = dni[j+1]
                dni[j+1] = temp
    return dni

def hlavny_cyklus(pocet,dni,i = 0,vysledok = 0):
    j = len(dni)-1
    for k in range(pocet):
        vysledok += dni[j] - dni[i]
        i += 1
        j -= 1
    return vysledok 

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        pocet = input("Zadajte pocet dni: ").strip()
        if pocet.isdigit() == True:
            dni = nacitanie(pocet)
            print(dni)
            print(hlavny_cyklus(int(pocet),dni))
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo")
