listy = ["B","?","B"]
cisla = []
cislo = 0
cisla1 = []
i = 0
zvysok = 0
docasne = 0
slovo = ""
zvysok1 = 0

for pismeno in listy:
    if pismeno == "C":
        cislo = i
        cisla.append(cislo)
        
        
        
    if pismeno == "B":
        cislo = i
        cisla1.append(cislo)
        
    i += 1

if cisla != []:
    
    zvysok1 = int(cisla[0])%2
    docasne = zvysok1
    for cislo in cisla:
        zvysok1 = int(cislo)%2
        if zvysok1 == docasne:
            pass
        else:
            slovo = "koniec"
            break
        
if cisla1 != []:
    zvysok = int(cisla1[0])%2
    if cisla != []:
        if zvysok == zvysok1:
            slovo = "koniec"
    
    docasne = zvysok
    for cislo in cisla1:
        if slovo == "koniec":
            break
        zvysok = int(cislo)%2
        if zvysok == docasne:
            pass
        else:
            slovo = "koniec"
            break
    
if slovo == "koniec":
    print("NEda sa to spravit")
elif slovo == "":
    print("Da sa")
    
    
print(cisla)
print(cisla1)
