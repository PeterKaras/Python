pridanie = [6,12,16]
cas = [12,20,24,16,6]
k = 0
p = 0
indexy = []
for pismeno in pridanie:
    for pismeno1 in cas:
        if pridanie[p] == cas[k]:
            indexy.append(k)
        else:
            pass
        k += 1
    p += 1
    k = 0

print(indexy)
