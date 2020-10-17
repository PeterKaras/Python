class Main:
    def __init__(self,nums):
        self.nums = nums
        self.graph = {}
        self.prime_numbers = []

    def checking(self):
        for i in range(2):
            for j in range(len(self.nums[i])):
                if self.nums[i][j].isdigit():
                    pass
                else:
                    return "Revise"
        self.nums[0],self.nums[1] = self.nums[0].lstrip("0"),self.nums[1].lstrip("0")
        print(self.nums[0],self.nums[1])
        
    def main_loop(self):
        for i in range(2,10000):
            word = self.prime_number(i,int(i**0.5))
            if word != "rdy":
                self.prime_numbers.append(str(i))
                
        for number in self.prime_numbers:
            self.making_dic(number)
        return self.BFS_SP(self.graph,self.nums[0],self.nums[1])

    def making_dic(self,number):
        self.ones(int(number))
        self.finding_prime(number,10)
        self.finding_prime(number,100)
        self.finding_prime(number,1000)

    def ones(self,number):
        number1 = number-(number%10)
        for i in range(1,10):
            if str(number1+i) in self.prime_numbers:
                self.graph.setdefault(str(number),[]).append(str(number1+i))
                
    def finding_prime(self,number,counter):
        if counter == 10 and len(number)==2:
            number1 = int(number)-(int(number[0])*10)
        elif counter == 10 and len(number)==3:
            number1 = int(number)-(int(number[1])*10)
        elif counter == 10 and len(number)==4:
            number1 = int(number)-(int(number[2])*10)      
        elif counter == 100 and len(number)==3:
            number1 = int(number)-(int(number[0])*100)
        elif counter == 100 and len(number)==4:
            number1 = int(number)-(int(number[1])*100)
        elif counter == 1000 and len(number)==4:
            number1 = int(number)-(int(number[0])*1000)
        else:
            number1 = int(number)
            
        for i in range(0,10):
            if str(number1+counter*i) in self.prime_numbers and \
               str(number1+counter*i) not in self.graph[number]:
                self.graph.setdefault(str(number),[]).append(str(number1+counter*i))

    def prime_number(self,number,indicator):
        amount = 0
        for i in range(1,indicator+1):
            if number%i==0:
                amount += 1
            if amount == 2:
                return "rdy"
            
    def BFS_SP(self,graph, start, goal): 
        explored = [] 
        queue = [[start]] 
        if start == goal: 
            return "0"

        while queue: 
            path = queue.pop(0) 
            node = path[-1] 
            if node not in explored: 
                neighbours = graph[node] 
                  
                for neighbour in neighbours:
                    new_path = list(path) 
                    new_path.append(neighbour) 
                    queue.append(new_path)
                    
                    if neighbour == goal:  
                        return len(new_path)-1
                explored.append(node) 
        return "-1"
            
    def __str__(self):
        if self.checking() != "Revise":
            return str(self.main_loop())
        else:
            return "Revise"

loop = input("Zadajte pocet cyklov: ").strip()
if loop.isdigit() and len(loop)>= 1:
    while int(loop)!=0:
        nums = input("Zadajte vase cisla: ").split()
        if len(nums)==2 and nums[1].isdigit() and nums[0].isdigit():
            print(Main(nums))
        else:
            print("Nezadali ste cislo!")
            continue
        loop = int(loop)-1
else:
    print("Nezadali ste cislo!")
