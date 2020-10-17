zistenie = ['a', 'h', 'o', 'o', 'j', '.','a', 'h', 'o', 'o', 'o', 'j',"."]
p = 0
slovo2 = ['a', 'h', 'o', 'j']
rozklad = []
for pismeno2 in slovo2:
    pismeno = slovo2[p]
    for pismeno1 in zistenie:
    
        print(pismeno)
        if pismeno1 == pismeno:
            rozklad.append(pismeno)
        elif pismeno1 == ".":
            rozklad.append(pismeno1)
        else:
            pass
                
    p += 1
    print(rozklad) 
    rozklad = []
