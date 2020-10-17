pole = ['.^.', '.<..v', 'v..']
i = 1
j = 1
pocet = 0
for m in range(6):
    print(i , j)
    print("pole",pole[i])
    print("jalo",pole[i][j-1])
    if pole[i][j-1] != ".":
        pocet += 1
        print("vpoho")
        print("jalo",pole[i][j-1])
        break
    j -= 1
    if j == 0:
        break
print(pocet)
