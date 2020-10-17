for j in range(len(pole)):
    if j < 3 or j > policka-4:
        spojitko += pole[j]
        if j == 2 or j == policka-1:
            print("   ",spojitko)
            spojitko = "" 
    elif j >= 3 and j < policka-(policka-(rozhranie-2)) or j > policka-(rozhranie-1):
        if pocitadlo == 0:
            spojitko += pole[j]
            spojitko += "O"
            pocitadlo += 1
        elif pocitadlo == 1:
            spojitko += pole[j]
            print("   ",spojitko)
            spojitko = ""
            pocitadlo = 0
            continue
    elif (j >= policka-(policka-(rozhranie-2))-1 and  j < policka-(policka-(rozhranie-2))+rozhranie-1) or \
         (j > ((policka-(policka-(rozhranie-2))+rozhranie-1)+1) and j < (policka-(rozhranie-1))+1):
        if j == (policka-(policka-(rozhranie-2))-1)+hranica+1 or j ==((policka-(policka-(rozhranie-2))+rozhranie-1)+1)+hranica+1: 
            spojitko += "O"
            spojitko += pole[j]
        else:
            spojitko += pole[j]
        if j == policka-(policka-(rozhranie-2))+rozhranie-2 or j == policka-(rozhranie-1):
            print(spojitko)
            spojitko = ""
    else:
        if pocitadlo == 0:
            spojitko += pole[j]
            spojitko += "O"*4
            spojitko += " X "
            spojitko += "O"*4
            pocitadlo += 1
        else:
            spojitko += pole[j]
            pocitadlo = 0
            print(spojitko)
            spojitko = "" 
