crosswords=[['c', 'd', 'o', 'g'], ['a', 'a', 'c', 'm'], ['t', 'x', 't', 't'], ['t', 'e', 't', 'k']]
words=['cat', 'dog']
horizontal_match_found = [False,False]
word_index=0  

def capitalize_word_in_crossword(crosswords, words):
    for rownum, row in enumerate(crosswords):
        print(rownum, row)
        word_index=0
        for word in words:
            find_index=''.join(row).lower().find(word)
            if find_index<-1:
                find_index=''.join(row).lower().find(word[::-1])
            if find_index>-1:
                print(find_index)
                for i in range(find_index, len(word)+find_index):
                    crosswords[rownum][i]=crosswords[rownum][i].upper()

                if not horizontal_match_found[word_index]:
                    horizontal_match_found[word_index]=True
            word_index+=1

    for colindex in range(len(crosswords[0])):
        word_index=0
        for word in words:
            if not horizontal_match_found[word_index]:
                colvalues=[row[colindex] for row in crosswords]
                find_index=''.join(colvalues).lower().find(word)
                if find_index<-1:
                    find_index=''.join(row[::-1]).lower().find(word)
                if find_index>-1:
                    for i in range(find_index, len(word)+find_index):
                        crosswords[i][colindex]=crosswords[i][colindex].upper()
                horizontal_match_found[word_index]=True
            word_index+=1
            
    l = 4
    print("C",[crosswords[i][i] for i in range(l)])
    
    return crosswords

print("Input: "+str(crosswords))
print("Output: "+str(capitalize_word_in_crossword(crosswords, words)))
