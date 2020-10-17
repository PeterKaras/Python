crosswords = [['P', 'E', 'T', 'O', 'A', 'X'],
              ['J', 'E', 'X', 'X', 'H', 'X'],
              ['A', 'X', 'P', 'X', 'O', 'X'],
              ['N', 'N', 'X', 'S', 'J', 'X'],
              ['O', 'X', 'O', 'X', 'I', 'X'],
              ['X', 'X', 'X', 'S', 'X', 'L']]

horizontal_match_found = [False,False]
fdiag = []
bdiag = []
guess = ["EPSIL","NOS"]
hranica = 0
zaciatok=0
word = ""
word_index = 0
l = 3

for i in range(len(crosswords)):
    #print("i",i)
    hranica = 0
    zaciatok = i
    for j in range(len(crosswords[i])):
        for k in range(len(crosswords)):
            if zaciatok == len(crosswords) or hranica == -1:
                continue
            word += crosswords[zaciatok][hranica]
            #print(crosswords[zaciatok][hranica])
            p = str(zaciatok)+str(hranica)
            fdiag.append(list(p))
            hranica -= 1
            zaciatok += 1
        print(word)
        #print(fdiag)
        #print(horizontal_match_found)
        for pole in guess:
            #print("k",word)
            if not horizontal_match_found[word_index]:
                print("k",word)
                print(horizontal_match_found)
                find_index=''.join(word).upper().find(pole)
                print(find_index)
                if int(find_index)<=-1:
                    find_index=''.join(word[::-1]).upper().find(pole)
                    print("index",find_index)
                if find_index>-1:
                    for index in range(find_index, len(pole)+find_index):
                        k = int(fdiag[index][0])
                        colindex = int(fdiag[index][1])
                        crosswords[k][colindex]=crosswords[k][colindex].lower()
                    if not horizontal_match_found[word_index]:
                        horizontal_match_found[word_index]=True
            word_index+=1
        word_index = 0
        zaciatok = i
        hranica = j+1
        fdiag = []
        word = ""
        if hranica == len(crosswords[i]):
            break
    hranica = 0
print(crosswords)
