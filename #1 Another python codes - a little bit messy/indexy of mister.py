"""field = [['*', '*', '*'], ['*', 'O', '*'], ['*', 'O', '*'], ['*', 'O', '*'],
                 ['*', '*', '*', '*', '*', 'O', '*', '*', '*', '*', '*'],
                 ['*', 'O', 'O', 'O', 'O', ' ', 'O', 'O', 'O', 'O', '*'],
                 ['*', '*', '*', '*', '*', 'O', '*', '*', '*', '*', '*'],
                 ['*', 'O', '*'], ['*', 'O', '*'], ['*', 'O', '*'], ['*', '*', '*']]"""

field =  [['*', '*', '*'], ['*', 'O', '*'], ['*', 'O', '*'],
                 ['*', '*', '*', '*', 'O', '*', '*', '*', '*'],
                 ['*', 'O', 'O', 'O', ' ', 'O', 'O', 'O', '*'],
                 ['*', '*', '*', '*', 'O', '*', '*', '*', '*'],
                 ['*', 'O', '*'], ['*', 'O', '*'], ['*', '*', '*']]

"""indexy = [[8,9,10],[7,11],[6,12],[5,13],[1,2,3,4,14,15,16,17,18],
               [39,19],[38,37,36,35,34,24,23,22,21,20],[33,25],[32,26],[31,27],
               [30,29,28]]"""
indexy = [[7, 8, 9],
          [6, 10],
          [5, 11],
          [1, 2, 3, 4, 12, 13, 14, 15],
          [32,16],
          [17, 18, 19, 20, 28, 29, 30, 31],
          [27, 21],
          [26, 22], [25, 24, 23]]
home = [9, 10, 18, 17, 19]
env = 9
separator = (9//2)+1
permission = 3
align_players = ["A","B"]
path =[[12,15],[20,26]]
maxi_steps = 32
"""[[7, 8, 9], [6, 10], [5, 11],
 [1, 2, 3, 4, 12, 13, 14, 15],
 [16, 32], [17, 18, 19, 20, 28, 29, 30, 31], [21, 27],
 [22, 26], [23, 24, 25]]"""

print(indexy[separator-1][-1])
for i in range(len(home)):
    if int(maxi_steps) < int(home[i]) <= int(maxi_steps)+permission:
        pozicia = int(home[i])-int(maxi_steps)
        field[separator-1][pozicia] = "A"
    elif indexy[separator-1][-1] < int(home[i]) <= indexy[separator-1][-1]+permission:
        pozicia = (separator-1)+(int(home[i])-indexy[separator-1][-1])
        print("C")
        print(pozicia)
        field[separator-1][pozicia] = "C"
    elif indexy[0][1] < int(home[i]) <= indexy[0][1]+permission:
        if int(home[i]) == indexy[0][1]+permission:
            field[separator-2][separator-1] = "B"
        else:
            pozicia = (int(home[i])-indexy[0][1])
            field[pozicia][1] = "B"     
    elif indexy[-1][1] < int(home[i]) <= indexy[-1][1]+permission:
        if int(home[i]) == indexy[-1][1]+permission:
            field[separator][separator-1] = "D"
        else:
            pozicia = (int(home[i])-indexy[-1][1])+separator+1
            field[pozicia][1] = "D"

print(field)
"""for i in range(len(indexy)):
    if 11 in indexy[i]:
        print(indexy[i].index(11))
print(indexy[separator])
print(separator)
for i in range(len(path)):
    for j in range(len(path[i])):
        for k in range(len(field)):
            if path[i][j] in indexy[k]:
                print(indexy[k],path[i][j])
                position = indexy[k].index(path[i][j])
                print("this is first",position)
                if separator == k or separator-2 == k:
                    print(k,separator,indexy[k],path[i][j])
                    if position > separator-2:
                        position += 1
                elif separator-1 == k:
                    print(k,separator,indexy[k],path[i][j],"ok")
                    if position > 0:
                        position += int(env)-3
                elif k == 0 or k == len(field)-1:
                    pass
                else:
                    if position > 0:
                        position += 1
                print(k,position)
                field[k][position] = align_players[i]
                print(field)
            else:
                pass
print(field)
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == "*" or field[i][j] == " " or field[i][j] == "O":
            pass
        else:
            field[i][j] = "*"
print(field)"""
"""env = 9
indexy = [[] for column in range(int(env))] 
print(indexy)
separator = 5
shift = 3
pocet = 1
slovo = "down"
koniec = 0
while pocet != ((env-1)*4)-1:       
    for j in range(len(field[shift])):
        print(field[shift])
        if field[shift][j] == "O":
            break
        else:
            indexy[shift].append(pocet)
        pocet += 1
        print(shift)
        koniec += 1
        if koniec == 32:
            break

    if slovo == "up":
        shift += 1
    else:
        shift -= 1
        
    if shift == -1:
        shift += 2
        print("somtu")
        slovo = "up"
    elif shift == env-1:
        slovo = "down"

    print(indexy)
    #koniec += 1
    if koniec == 32:
        break"""

