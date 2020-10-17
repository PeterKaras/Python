pole = ['*', '*', '*', '*', '*', '*',
        '*', '*', '*', '*','*', '*',
        '*', '*', '*', '*', '*', '*',
        '*', '*', '*','*', '*', '*',
        '*', '*', '*','*', '*', '*'
        '*', '*', '*']
paths = []

print(len(pole))
policka = len(pole)
rozhranie = 11
hranica = ((rozhranie-1)//2)
indexovanie = [[8,9,10],[7,11],[6,12],[5,13],[40,1,2,3,4,14,15,16,17,18],
               [39,19],[38,37,36,35,34,24,23,22,21,20],[25,33],[26,32],[27,31],
               [30,29,28]]

spojitko = ""
pocitadlo = 0
l = 1

for j in range(rozhranie):
    if j == 0 or j == rozhranie-1:
        paths.append(list("*"*3))
    elif j == hranica-1 or j == hranica+1:
        paths.append(list("*"*(rozhranie-1)))
        if rozhranie >= 13:
            paths[j].insert((len(paths[j])//2)," ")
        else:
            paths[j].insert((len(paths[j])//2),"O")
    elif j == hranica:
        paths.append(list("*"*2))
        for i in range(rozhranie):
            if i == 0 or i == rozhranie-1:
                pass
            elif (i <= (4) or i >= (rozhranie-5)):
                paths[j].insert(i,"O")
                print(i)
            else:
                paths[j].insert(i," ")
    else:        
        paths.append(list("*"*2))
        if j <= 4 or j >= rozhranie-5:
            paths[j].insert(1,"O")
            #paths[j].insert(1," ")
        else:
            paths[j].insert(1," ")
print(paths)
zvysok = paths
print("zvysok",zvysok) 
for j in range(rozhranie):
    path = "".join(paths[j])
    print("{:^70}".format(path))
p = 0

#maze???? asi hej pojdem po * a ked narazim na nieco ine otoci sa alebo ked bude koniec pola pojdem dole alebo hore!
for i in range(rozhranie):
    if 7 in indexovanie[i]:
        print(indexovanie[i])
        print()
        pozicia = indexovanie[i].index(7)
        print(pozicia)
        for j in range(len(paths[i])):
            print(paths[i][j])
            if paths[i][j] == "*":
                #print("tu")
                if p == int(pozicia):
                    print("tu")
                    paths[i][j] = "A"
                    print(paths[i])
                    break
                p += 1
        for k in range(rozhranie):
            path = "".join(paths[k])
            print("{:^70}".format(path))
        paths = []
        paths = zvysok
        print("toto",zvysok)
        break
    #paths.append(zvysok)
    p = 0
    #print(paths)
        
        
