import math
from fractions import Fraction
def kontrola(zaciatok,pocet,ok = "ok"):
    for cislo in zaciatok:
        if cislo.replace(".","",1).isdigit() == True:
            pass
        else:
            ok = "ne"
            return ok
        pocet -= 1   
    if pocet != 0:
        ok = "ne"
        return ok
    else:
        return ok

def nacitanie(pocetnost,zaciatok, znak = ""):
    pole = []
    while int(pocetnost) != 0:
        cisla = input("Zadajte cisla: ").split()
        znak = kontrola(cisla,pocet = 2)
        if znak == "ok":
            znak = separacia(cisla,zaciatok)
            if znak[0] == "ok":
                pole.append(znak[1])
                print(pole)
            else:
                pass
        else:
            continue
        pocetnost = int(pocetnost) - 1 
    return pole

def separacia(cisla,zaciatok,znak = "Ne", uhol = 0):
    vysledok = ((((int(zaciatok[0]) - int(cisla[0]))**2)) + (((int(zaciatok[1]) - int(cisla[1]))**2)))**(1/2)
    if float(vysledok) <= float(zaciatok[2]):
        znak = "ok"
        uhol = uhly(cisla,zaciatok)
        return znak,uhol
    else:
        return znak

def uhly(cisla,zaciatok):
    x = int(cisla[0]) - int(zaciatok[0])
    y = (int(cisla[1]) - int(zaciatok[1]))
    tangens = math.degrees(math.atan2(y, x))
    if tangens < 0:
          tangens = 360 + tangens
    else:
        pass
    return tangens

def zoradenie(cisla,j = 0, i = 0):
    for i in range(len(cisla)-1,0,-1):
        for j in range(i):
            if int(cisla[j]) > int(cisla[j+1]):
                   temp = cisla[j]
                   cisla[j] = cisla[j+1]
                   cisla[j+1] = temp
    return cisla

def koniec(cisla,i = 0, j = 0,maxi = 0,pocet = 0,ostat = 0):
    for cislo in cisla:
        for cislo1 in cisla:
            if j <= i:
                pass
            else:
                if (int(cisla[j]) - int(cisla[i])) <= 180:
                    ostat = 180 - int(cisla[j])
                    pocet += 1
                else:
                    zostatok = 360 - int(cisla[j])
                    if zostatok <= ostat:
                        pocet += 1 
            j += 1
        i += 1
        j = 0
        if pocet > maxi:
            maxi = pocet
        pocet = 0   
    return maxi+1
    
cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        zaciatok = input("Zadajte zaciatok a dosah: ").split()
        znak = kontrola(zaciatok,pocet = 3)
        if znak == "ok":
            pocetnost = input("Zadajte pocet cisiel na zadavanie: ").strip()
            if pocetnost.isdigit() == True:
                cisla = nacitanie(pocetnost,zaciatok)
                cisla = zoradenie(cisla)
                print(koniec(cisla))
            else:
                print("Nezadali ste cele alebo spravne cislo/cisla! Skúste znovu.\n")
                continue
        else:
            print("Nezadali ste cislo/cisla!\n")
            continue
        cyklus = int(cyklus) - 1
        cisla = []
else:
    print("Nezadali ste cislo!")
