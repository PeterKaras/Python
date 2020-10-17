
crosswords = [['M', 'P', 'T', 'O', 'A', 'X'],
              ['J', 'L', 'O', 'X', 'H', 'X'],
              ['A', 'X', 'I', 'T', 'O', 'X'],
              ['K', 'N', 'X', 'S', 'J', 'X'],
              ['O', 'A', 'O', 'S', 'P', 'K'],
              ['O', 'R', 'R', 'S', 'L', 'E']]

horizontal_match_found = [False,False]
guess = ["JAKO","AHOJ"]




for colindex in range(len(crosswords[0])):
    word_index=0
    for word in guess:
        if not horizontal_match_found[word_index]:
            colvalues =[row[colindex] for row in crosswords]
            print(colvalues)
            find_index=''.join(colvalues).upper().find(word)
            if find_index<=-1:
                find_index=''.join(colvalues).upper().find(word[::-1])
            if find_index>-1:
            
                for i in range(find_index, len(word)+find_index):
                    crosswords[i][colindex]=crosswords[i][colindex].lower()
                if not horizontal_match_found[word_index]:
                    horizontal_match_found[word_index]=True
        word_index+=1

print(crosswords)
