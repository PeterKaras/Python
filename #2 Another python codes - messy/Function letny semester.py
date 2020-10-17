x = float(input("Zadajte realne cislo X: "))
n = float(input("Zadajte cele cislo N: "))
y = float(input("Zadajte realne cislo Y: "))

mocnina = x**n
prava_strana = 1/mocnina


if x == 0:
    print("Zadali ste X = 0")
elif prava_strana > y:
    print("Plati")
elif prava_strana < y:
    print("Neplati")
