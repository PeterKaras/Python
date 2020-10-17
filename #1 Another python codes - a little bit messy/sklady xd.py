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

    def loading(self):
        amount = int(self.range_field[0])
        i = 0
        while amount != 0:
            symbols = input("Zadajte vase znaky: ").strip()
            if self.checking(symbols,i) != "Revise" and len(symbols)==int(self.range_field[1]):
                self.field.append(symbols)
            else:
                print("Wrong input! One more time!")
                continue
            amount -= 1
            i += 1
            
    def checking(self,symbols,i):
        for badge in enumerate(symbols):
            if badge[1].upper() == "X" and self.central == None:
                self.central = (str(i)+" "+str(badge[0])).split(" ")
            elif badge[1] == "$":
                indexy = str(i)+" "+str(badge[0])
                self.sklady.append(indexy.split(" "))
            elif badge[1].isdigit():
                if int(self.mini) > int(badge[1]):
                    self.mini = int(badge[1])
            else:
                return "Revise"
    
    def main_loop(self):
        print(self.field)
        print(self.central)
        print(self.sklady)
        print(self.bfs(self.field,self.field,(int(self.central[0]), int(self.central[0]))))

    def bfs(self,grid1,second_grid, start,i = 0):
        wall, goal = "#" , "X"
        seen=[]
        overall=[]
        width, height = int(self.range_field[1]), int(self.range_field[0])
        queue = collections.deque([[start]])
        seen.append([start])
        while queue:
            path = queue.popleft()
            #print("patH",path)
            x, y = path[-1]
            if i == 0:
                i += 1
            else:
                grid1 = self.transforming_grif(second_grid,second_grid[y][x])
            grid = grid1[len(grid1)-int(self.range_field[0]):len(grid1)]
            
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and path+[(x, y)] not in seen:
                    queue.append(path + [(x2, y2)])
                    overall.append(path+[(x, y)])
                seen.append(path+[(x,y)])
        print(seen)
        return overall

    """def displaying(self,overall):
        #print(overall)
        new_field = [list(self.field[i]) for i in range(len(self.field))]
        for i in overall:
            #print(i)
            new_field[int(i[1])][int(i[0])] = "X"
            
        for i in range(len(new_field)):
            print("".join(new_field[i]))
        #print()"""
        
    def transforming_grif(self,field,position,listed_field=[]):
        print(position)
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
            #print("".join(listed_field[i]))
        #print()
        return new_field
    

    def __str__(self):
        if self.loading() != "Revise":
            return str(self.main_loop())
        else:
            return "Revise"
            
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
