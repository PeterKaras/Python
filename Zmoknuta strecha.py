import collections
import sys
class Loading:
    def __init__(self):
        self.numbers = []
        self.comparision=[]
    
    def loading_inputs(self,amount):
        while amount != 0:
            row = input("Zadajte cisla: ").split()
            if len(row) == self.columns:
                if self.checking(row) != "Revise":
                    self.numbers.append(row)
                    self.comparision.append(row)
                    amount -= 1
                else:
                    return "Revise"

    def checking(self,row):
        for number in row:
            if number.isdigit():
                pass
            else:
                return "Revise"
                
class Main(Loading):
    def __init__(self,initial):
        super().__init__()
        self.rows = int(initial[0])
        self.columns = int(initial[1])

    def bfs(self,grid, start,indicator,mini = sys.maxsize):
        overall=[]
        queue = collections.deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if (x2 == int(self.columns)-1 or y2 == int(self.rows)-1 or y2 == 0 or x2 == 0) and int(grid[y2][x2]) <= indicator:
                    return "-1","-1"
                elif 0 <= x2 < int(self.columns) and 0 <= y2 < int(self.rows) and int(grid[y2][x2]) <= indicator and \
                     (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
                    overall.append(path + [(x2, y2)])   
                else:
                    if 0 <= x2 < int(self.columns) and 0 <= y2 < int(self.rows) and int(grid[y2][x2])<mini and (x2, y2) not in seen:
                        mini = int(grid[y2][x2])         
        return overall,mini
        
    def main_loop(self,result=0):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if i == 0 or i == self.rows-1 or j == 0 or j == self.columns-1:
                    continue
                else:
                    trails,mini= self.bfs(self.numbers, (j,i),int(self.numbers[i][j]))
                    if trails == "-1":
                        pass
                    elif len(trails) == 0:
                        result += mini - int(self.numbers[i][j])
                        self.numbers[i][j] = str(mini)
                    else:
                        for position in trails:
                            for pos in position:
                                result += mini - int(self.numbers[pos[1]][pos[0]])
                                self.numbers[pos[1]][pos[0]] = str(mini)
        return result
      
    def __str__(self):
        if self.loading_inputs(self.rows) != "Revise":
            return str(self.main_loop())
        else:
            return "REVISE!"

loop = input("Zadajte pocet cyklov: ").strip()
if loop.isdigit() and len(loop)>=1:
    while int(loop)!=0:
        initial = input("Zadajte pocet riadkov a stplcov: ").split()
        if len(initial)==2 and initial[0].isdigit() and initial[1].isdigit():
            print(Main(initial))
        else:
            print("Nezadali ste cislo/a!")
            continue
        loop = int(loop)-1
else:
    print("Nezadali ste cislo!")
