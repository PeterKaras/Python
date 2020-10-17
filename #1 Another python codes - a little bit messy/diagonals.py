crosswords = [['M', 'P', 'T', 'O', 'A', 'X'],
              ['J', 'L', 'O', 'X', 'H', 'X'],
              ['A', 'X', 'I', 'T', 'O', 'X'],
              ['K', 'N', 'X', 'S', 'O', 'X'],
              ['K', 'A', 'O', 'S', 'P', 'K'],
              ['O', 'R', 'R', 'S', 'L', 'E']]
horizontal_match_found = [False,False,False,False]
fdiag = []
bdiag = []
guess = ["EPSIL","NOS","POTOK","KAR"]
hranica = 0
zaciatok=0
word = ""
word_index = 0
l = 3

for i in range(len(crosswords)):
    hranica = 0
    zaciatok = i
    for j in range(len(crosswords[i])):
        for k in range(len(crosswords)):
            if zaciatok == len(crosswords) or hranica == len(crosswords[0]):
                continue
            word += crosswords[zaciatok][hranica]
            #print(crosswords[zaciatok][hranica])
            p = str(zaciatok)+str(hranica)
            fdiag.append(list(p))
            hranica += 1
            zaciatok += 1
        #print(word)
        zaciatok = i
        hranica = j+1
        for pole in guess:
            if not horizontal_match_found[word_index]:
                find_index=''.join(word).upper().find(pole)
                if find_index<=-1:
                    find_index=''.join(word).upper().find(pole[::-1])
                if find_index>-1:
                    print(find_index)
                    print(word)
                    print(fdiag)
                    for index in range(find_index, len(pole)+find_index):
                        k = int(fdiag[index][0])
                        colindex = int(fdiag[index][1])
                        print(k,colindex)
                        crosswords[k][colindex]=crosswords[k][colindex].lower()
                    if not horizontal_match_found[word_index]:
                        horizontal_match_found[word_index]=True
            word_index += 1
        word_index = 0
        word = ""  
        fdiag = [] 
                        
        """#word_index = 0
        zaciatok = i+1
        hranica = j+1
        fdiag = []
        word = ""
        if hranica == len(crosswords[i]):
            break
    hranica = 0
    #word_index = 0"""
print(crosswords)
"""max_col = len(crosswords[0])
max_row = len(crosswords)
min_bdiag = -max_row + 1
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
print(fdiag)
print(bdiag)
for x in range(max_col):
    for y in range(max_row):
        fdiag[x+y].append(crosswords[y][x])
        print(crosswords[y][x])
        bdiag[x-y-min_bdiag].append(crosswords[y][x])
print(fdiag)
print(bdiag)"""
    
