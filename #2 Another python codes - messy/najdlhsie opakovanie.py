pismena = input("Zadajte pismena :")
docasne = ""
vysledok = 0
pocet = 1

for pismeno in pismena:
    if pismeno == docasne:
        pocet += 1
    else:
        if vysledok < pocet:
            vysledok = pocet
        pocet = 1
    docasne = pismeno

print("Najdlhsie poradie bolo:",vysledok)
