pocet = int(input("Zadajte pocet cyklov: "))
slovnik = {}
indexy = []
vstupy = []
cisla = []
zoradenie = []
i = 0
j = 0
spojitko = ""
listy = []
pre_s = []

while pocet != 0:
    vstup = input("Zadajte cislo pre kt chcete zadavat: ").strip()
    cislo = input("Zadajte cislo: ").strip()
    cisla.append(cislo)
    vstupy.append(vstup)
    pocet -= 1
    
for pismeno in vstupy:
    zoradenie.append(pismeno)
    
for i in range(len(zoradenie)-1,0,-1):
    for j in range(i):
        if int(zoradenie[j]) > int(zoradenie[j+1]):
            temp = zoradenie[j]
            zoradenie[j] = zoradenie[j+1]
            zoradenie[j+1] = temp
i = 0
j = 0
for cislo in zoradenie:
    if cislo == spojitko:
        pass
    else:
        listy.append(cislo)
        
    spojitko = cislo
    
zoradenie = []
for cislo in range(len(listy)):
    for cislo1 in vstupy:
        if cislo1 == listy[i]:
            indexy.append(j)
            
        j += 1
        if j == len(vstupy):
            break
    
    for cislo1 in indexy:
        pre_s.append(cisla[cislo1])

    slovnik.update({listy[i]:pre_s})

    pre_s = []
    indexy = []
    i += 1
    j = 0
    if i == len(vstupy):
        break
    
print(slovnik)
