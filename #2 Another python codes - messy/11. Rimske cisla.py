cislo = 0
vysledok = 0
rimske = input("Zadajte rimske cislo: ")
rimske1 = rimske[::-1]

for pismeno in rimske1:
    if pismeno == "M":
        pismeno = 1000
    elif pismeno == "D":
        pismeno = 500
    elif pismeno == "C":
        pismeno = 100
    elif pismeno == "L":
        pismeno = 50
    elif pismeno == "X":
        pismeno = 10
    elif pismeno == "V":
        pismeno = 5
    else:
        pismeno = 1
    
    if cislo > pismeno:
        vysledok -= pismeno
    elif cislo < pismeno:
        vysledok += pismeno
    elif cislo == pismeno:
        vysledok += pismeno

    if vysledok < 0:
        vysledok *= -1 
    cislo = pismeno
    
print(vysledok)
