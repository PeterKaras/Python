class Main:
    def __init__(self,initial):
        self.cities = int(initial[0])
        self.amount_trails = int(initial[1])
        self.trails = {}
        self.beggining = 0
        self.end = 0
        self.numbers = []

    def loading(self):
        for i in range(self.amount_trails):
            trail = input("Zadajte suradnice zeleznice: ").split()
            if len(trail)== 2 and trail[0].isdigit() and trail[1].isdigit():
                self.trails.setdefault(int(trail[0]),[]).append(int(trail[1]))
                self.trails.setdefault(int(trail[1]),[]).append(int(trail[0]))

                if i == 0:
                    self.beggining = int(trail[0])
                self.numbers.append(int(trail[0]))
                self.end = int(trail[1])
            else:
                return "Prepracovat"
 
    def BFS_SP(self,graph, start, goal,result=[]): 
        explored = []     
        queue = [[start]]
        if start == goal:
            return 0
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored: 
                if node not in self.numbers:
                    pass
                else:
                    neighbours = graph[node]
                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour == goal:
                            return new_path
                explored.append(node)
        return 0

    def highway(self,numbers,blocked =[],new_list=[]):
        self.numbers = []
        self.trails_1 = {}
        for number in range(1,self.cities+1):
            if number not in numbers:
                for znak in self.trails:
                    if number in self.trails[znak]:
                        blocked.append(znak)
            else:
                for znak in self.trails:
                    if znak == number:
                        blocked.extend(self.trails[znak])
                    else:
                        if number in self.trails[znak]:
                            blocked.append(znak)

            for i in range(number,self.cities+1):
                if i not in blocked and i != number:
                    new_list.append(i)
            if len(new_list) != 0:
                self.numbers.append(number)
                self.trails_1.update({number:new_list})
            blocked = []
            new_list= []  

    def comma(self,znak,pocet=0):
        for pismeno in str(znak):
            if pismeno == ",":
                pocet += 1
        return pocet
                         
    def hlavny_cyklus(self):
        znak = self.BFS_SP(self.trails,self.beggining,self.end)
        amount = self.comma(znak)
        if znak == 0:
            return "-1"
        elif amount > 1:
            return amount
        else:
            self.highway(self.numbers)
            znak2 = self.BFS_SP(self.trails_1,self.beggining,self.end)
            return self.comma(znak2)
              
    def __str__(self):
        if self.loading() != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return "Prepracovat"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>=1:
    while int(cyklus)!=0:
        initial = input("Zadajte pocet miest a zeleznice: ").split()
        if len(initial)==2 and initial[0].isdigit() and initial[1].isdigit():
            print(Main(initial))
        else:
            print("Nezadali cisla!")
            continue
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")
