import sys
import itertools
import collections
class Main:
    def __init__(self,range_field):
        self.range_field = range_field
        self.sklady = []
        self.field = []
        self.mini= sys.maxsize
        self.central = None

    def loading(self,field =[]):
        for i in range(int(self.range_field[0])):
            symbols = input("Zadajte vase znaky: ").strip()
            if self.checking(symbols,i) != "Prepracovat":
                self.field.append(symbols)
            else:
                return "Prepracovat"

    def checking(self,symbols,i):
        for badge in enumerate(symbols):
            if badge[1].upper() == "X":
                self.central = (str(i)+" "+str(badge[0])).split(" ")
            elif badge[1] == "$":
                indexy = str(i)+" "+str(badge[0])
                self.sklady.append(indexy.split(" "))
            elif badge[1].isdigit():
                if int(self.mini) > int(badge[1]):
                    self.mini = int(badge[1])
            else:
                return "Prepracovat"
        if len(symbols)!= int(range_field[1]):
            return "Prepracovat"

    def making_iteration(self,end_result,first_sum=0,second_sum=0,mini=sys.maxsize,cisla1=[]):
        print(end_result)
        for i in range(len(end_result)):
            for j in range(len(end_result)):
                for k in range(len(end_result)):
                    if k >= i and k <= i+j:
                        if k == i+j:
                            first_sum += int(end_result[k])
                        else:
                            first_sum += int(end_result[k])*2
                    else:
                        cisla1.append(end_result[k])
                        
                for badge in range(len(cisla1)):
                    if badge >= len(cisla1)-1:
                        second_sum += int(cisla1[badge])
                    else:
                        second_sum += int(cisla1[badge])*2

                if second_sum>=first_sum:
                    if second_sum<mini:
                        mini = second_sum
                else:
                    if first_sum<mini:
                        mini = first_sum
                        
                first_sum = 0
                second_sum = 0
                cisla1 = []
                if i == len(end_result)-1 or j == len(end_result)-i-1:
                    break
            if i == len(end_result)-1:
                break
        return mini

    def portraying(self,trails,display="\n"):
        environment = [list(row) for row in self.field] 
        for trail in trails:
            for position in trail:
                environment[position[1]][position[0]] = "X"
        for row in environment:
            display += "".join(row)
            display += "\n"
        print("{}".format(display))
        
    def alignment(self,end_result):
        for i in range(len(end_result)-1,0,-1):
            for j in range(i):
                if end_result[j] > end_result[j+1]:
                    temp = end_result[j]
                    end_result[j] = end_result[j+1]
                    end_result[j+1] = temp
        return end_result

    def finding_sum(self,path,level=0):
        first=path.pop(0)
        level = self.field[path[0][1]][path[0][0]]
        second=path.pop(0)
        pocet=0
        for position in path:
            if level == "$":
                pocet += 2
            elif self.field[position[1]][position[0]] == "$":
                pocet += 2
            elif self.field[position[1]][position[0]] == level:
                pocet += 1
            else:
                pocet += 3
            level = self.field[position[1]][position[0]]

        path.insert(0,second)
        path.insert(0,first)
        return pocet+2

    def finding_path(self,path,my_list=[],k = 0,trails=[],indexy=[]):
        end_result=[]
        k = len(path)-1
        for i in range(len(self.sklady)):
            for j in range(len(path)):
                if len(path[j])>=1:
                    trail =path[j]
                    if trail[len(trail)-1][0] == int(self.sklady[i][1]) and trail[len(trail)-1][1] == int(self.sklady[i][0]):
                        trails.append(trail)
                        my_list.append(self.finding_sum(trail))
                if len(path[k])>=1:
                    trail = path[k]
                    if trail[len(trail)-1][0] == int(self.sklady[i][1]) and trail[len(trail)-1][1] == int(self.sklady[i][0]):
                        trails.append(trail)
                        my_list.append(self.finding_sum(trail))

                k -= 1
                if k < j:
                    break
            if len(my_list)== 0:
                return "-1"
            end_result.append(min(my_list))
            indexy.append(trails[my_list.index(min(my_list))])
            k = len(path)-1
            my_list = []
            trails=[]
        self.portraying(indexy)
        return str(self.making_iteration(self.alignment(end_result)))

    def transforming_grif(self,field,position,listed_field=[]):
        listed_field = [list(znak) for znak in field]
        if position == "$" or position=="X":
            pass
        else:
            for i in range(len(listed_field)):
                for j in range(len(listed_field[i])):
                    if str(field[i][j]) == "$" or str(field[i][j]) == "X":
                        pass
                    elif abs(int(position)-int(field[i][j])) >= 2:
                        listed_field[i][j] = "#"
        return self.creating_listed_list(listed_field)

    def creating_listed_list(self,listed_field,new_field=[]):
        for i in range(len(listed_field)):
            new_field.append("".join(listed_field[i]))
        return new_field
        
    def bfs(self,grid1,second_grid, start,overall=[],seen=[],i = 0):
        wall,clear, goal = "#" , ".", "$"
        width, height = int(self.range_field[1]), int(self.range_field[0])
        queue = collections.deque([[start]])
        seen.append([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if i == 0:
                i += 1
            else:
                grid1 = self.transforming_grif(second_grid,second_grid[y][x])
            grid = grid1[len(grid1)-int(self.range_field[0]):len(grid1)]
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in path and seen.count([x, y])<=4:
                    queue.append(path + [(x2, y2)])
                    if grid[y2][x2] == "$":
                        overall.append(path + [(x2, y2)])

            if seen.count([x, y])<=4:
                seen.append([x,y])
        return overall

    def hlavny_cyklus(self):
        path = self.bfs(self.field,self.field,(int(self.central[1]), int(self.central[0])))
        return str(self.finding_path(path))

    def __str__(self):
        if self.loading() != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return "Prepracovat"

cyklus  = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>=1:
    while int(cyklus)!= 0:
        range_field = input("Zadajte rozmedzie pola: ").split()
        if len(range_field)==2 and range_field[0].isdigit() and range_field[1].isdigit():
            print(Main(range_field))
        else:
            print("Nezadali ste cislo!")
            continue
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
