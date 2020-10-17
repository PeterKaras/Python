slova = [["p","e","t"],["p","e","t"],["p","e","t","t"],["p","p","e","t"]]
new = []
porov = "pet"
i = 0
zostatok = ""
for k in range(len(porov)):
    #print(porov[k])
    for i in range(len(slova)):
        #print(i)
        #print("i",slova[i])
        for j in range(len(slova[i])):
            #print("j",slova[i][j])
            if slova[i][j] == porov[k]:
                zostatok += slova[i][j]
            else:
                pass
        slovo = list(zostatok)
        new.append(slovo)
        zostatok = ""
    #print("no nic")
    print(new)
    new = []    

slovo = ""
zostatok = ""

for pismeno in slova:
    if zostatok == pismeno:
        pass
    else:
        slovo += str(pismeno)            
    zostatok = pismeno
print(slovo)
