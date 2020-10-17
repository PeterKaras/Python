paths = []
vzor = []
rozhranie = 11
hranica = (rozhranie-1)//2
indexovanie = [[8,9,10],[7,11],[6,12],[5,13],[40,1,2,3,4,14,15,16,17,18],
               [39,19],[38,37,36,35,34,24,23,22,21,20],[25,33],[26,32],[27,31],
               [30,29,28]]

paths = [['*', '*', '*'], ['*', 'O', '*'], ['*', 'O', '*'], ['*', 'O', '*'],
         ['*', '*', '*', '*', '*', 'O', '*', '*', '*', '*', '*'],
         ['*', 'O', 'O', 'O', 'O', ' ', 'O', 'O', 'O', 'O', '*'],
         ['*', '*', '*', '*', '*', 'O', '*', '*', '*', '*', '*'],
         ['*', 'O', '*'], ['*', 'O', '*'], ['*', 'O', '*'], ['*', '*', '*']]
for i in range(rozhranie):
    vzor.append(paths[i])
print(vzor)
slovo = ""
k = 0
for i in range(rozhranie):
    if 7 in indexovanie[i]:
        position = indexovanie[i].index(7)
        print(position)
        for j in range(len(paths[i])):
            print(paths[i][j])
            if paths[i][j] == "*":
                if k == position:
                    paths[i][j] = "A"
                    print(vzor)
                    paths[i][j] = "*"
                    print(vzor)
                    slovo = "koniec"
                    break
                else:
                    k += 1
            
        if slovo == "koniec":
            break
            
