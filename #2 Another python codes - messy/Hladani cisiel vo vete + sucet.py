def sucet_cisel(x):
    o = 0
    for n in x:
        if n.isdigit():
            o += int(n)
    return "Súčet čísel v texte je : " + str(o)
veta = input("Napíš lubovolnú vetu : \n")
veta = veta.split(" ")

print (sucet_cisel(veta))
