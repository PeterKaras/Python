def kontrola(cisla,posun = ""):
    for cislo in cisla:
        if cislo.isdigit() == True:
            posun = "ok"
        else:
            posun = "Ne"
            return posun
    return posun

def hlavny_cyklus(cisla,pocetnost = 0):
    while int(cisla[1]) < int(cisla[2]):
        pocetnost += 1
        cisla[1] = int(cisla[1]) + (int(cisla[1]) - int(cisla[0]))
    return pocetnost

pocet = input("Zadajte pocet sekvencii: ").strip()
if pocet.isdigit() == True:
    while int(pocet) != 0:
        cisla = input("Zadajte cisla: ").split()
        posun = kontrola(cisla)
        if posun == "ok":
            print(hlavny_cyklus(cisla))
        else:
            print("Nezadali ste cisla/cislo!")
        pocet = int(pocet) - 1
        cisla = []
else:
    print("Nezadali ste cislo!")
