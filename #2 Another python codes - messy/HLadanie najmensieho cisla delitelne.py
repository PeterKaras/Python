cislo = 20
delitel = 1
while True:
    zvysok = cislo%delitel
    
    if zvysok == 0:
        delitel += 1
    else:
        cislo +=1
        delitel = 1
    

    if delitel == 18:
        break

print(cislo)
