import random
slova = []
hladane_slovo = []
hladane_slovo1 = ""
docasne = ""
podjebnik1 = []
zhodnost = []
vysledok = ""
i = 0
dlzka = 0
podjebnik = ""

subor = open("hadanka.txt","r")
slovo = subor.readline()
while slovo:
    #print(slovo)
    slovo = subor.readline()
    if slovo == "":
        continue
    else:
        slova.append(slovo)

subor.close()
#print(slova)
hladane_slovo = random.choice(slova)
#print(hladane_slovo)

for pismeno in hladane_slovo:
    if pismeno == "\n":
        continue
    zhodnost.append(pismeno)
    
dlzka = len(hladane_slovo)-1
podjebnik = "-"*dlzka

for znak in podjebnik:
    podjebnik1.append(znak)
#print(podjebnik1)

while True:
    print("Zdravim ta pri hre Hadanka!")
    hadanie = input("Chces hadat po pismenkach stlac p: ").lower()
    while True:
        if hadanie == "p":
            hadane = input("Zadajte pismeno: ").lower()
            for pismeno in hladane_slovo:
                if hadane == pismeno:
                    podjebnik1[i] = pismeno
                i += 1
            for pismeno in podjebnik1:
                hladane_slovo1 += pismeno
            docasne = hladane_slovo1
            hladane_slovo1 = ""
            print(docasne)        

            i = 0
            if podjebnik1 == zhodnost:
                break
        else:
            print("Stlacil si nespravne klaves, zacni znova!\n")
            break         
          
    if podjebnik1 == zhodnost:
        break

        
for pismeno in podjebnik1:
    vysledok += pismeno
print("Slovo, kt si uhadol:",vysledok)
