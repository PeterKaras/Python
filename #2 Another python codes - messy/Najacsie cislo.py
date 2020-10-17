def max_cislo(y):
    cisla = []
    for x in y:
        if x.isdigit():
            x = int(x)
            cisla.append(x)
    cisla.sort()
    return("Naväčšie číslo je : " + str(cisla[-1]))
def max_slovo(y):
    slova = []
    for x in y:
        if x.isalpha():
            slova.append(x)
            slova.sort(key = len)
    return("Najdlhšie slovo je : " + str(slova[-1]))
veta = input("Napíš ľubovolnú vetu :\n").split(" ")
print (max_cislo(veta) + "\n" +  max_slovo(veta))
