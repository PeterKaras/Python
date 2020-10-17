def hlavny_cyklus(text,spolu = "",cislo = 0,ok = ""):
    for pismeno in text:
        if pismeno.isdigit() == True:
            spolu += str(pismeno)
        elif spolu != "":
            cislo += int(spolu)
            spolu = ""
            ok = "ok"
        else:
            continue
    return cislo,ok

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while cyklus != 0:
        text = input("Zadajte text: ").strip() + " "
        cislo = hlavny_cyklus(text)
        if cislo[1] == "ok":
            print(cislo[0])
        else:
            print("Ziadne číslo nebolo nájdené")
        cyklus = int(cyklus) - 1 
else:
    print("Nezadali ste cislo!")
    
