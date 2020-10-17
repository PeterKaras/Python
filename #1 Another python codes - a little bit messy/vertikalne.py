field = [['B', 'A', 'B', 'K', 'A', 'X'], ['A', 'H', 'O', 'P', 'K', 'A'],
         ['H', 'X', 'X', 'X', 'X', 'X'],
         ['O', 'L', 'P', 'P', 'A', 'A'], ['J', 'X', 'P', 'O', 'S', 'A']]

indexy = [['0', '1'], ['0', '4'], ['1', '0'], ['1', '5'], ['3', '4'], ['3', '5'], ['4', '5']]
pole = ""
k= 0

for i in range(len(indexy)):
    zaciatok = int(indexy[k][0])
    hranica = int(indexy[k][1])
    for j in range(5):
        pole += field[j][hranica]
    print(pole)
    k += 1
    pole = ""
