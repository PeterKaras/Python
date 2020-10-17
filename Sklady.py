from collections import defaultdict
import sys
import itertools
class Main:
    def __init__(self,interface):
        self.width = int(interface[0])
        self.lenght = int(interface[1])
        self.store = []
        self.shops = []
        self.envi = []
        self.initial_edges = []
        self.edges = defaultdict(list)
        self.weights = {}
        self.result = 0
        self.numbers = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
    
    def loading(self):
        amount = 0
        while amount!=self.width:
            row = input("Your input: ").strip()
            if len(row)== self.lenght and self.checking(row,amount) != "Revise":
                self.envi.append(list(row))
            else:
                print("Wrong Input!")
                continue
            amount += 1

    def checking(self,row,amount):
        for i in range(len(row)):
            if row[i].isdigit():
                pass
            elif row[i] == "X":
                self.store.append(amount)
                self.store.append(i)
            elif row[i] == "$":
                self.shops.append((str(amount)+" "+str(i)).split(" "))
            else:
                return "Revise"

    def main_loop(self):
        self.tuple_maker()
        beggining = str((self.store[0]*self.lenght)+self.store[1])
        for edge in self.initial_edges:
            self.add_edge(*edge)
        for position in self.shops:
            shop = str((int(position[0])*self.lenght)+int(position[1]))
            self.numbers.append(self.finding_sum(self.dijsktra(beggining, shop)))
        if 0 in self.numbers:
            return "-1"
        return self.making_iteration(self.numbers)
        
    def distance_counter_col(self,i,j):
        distance_col = abs(int(self.envi[i+1][j])-int(self.envi[i][j]))
        if distance_col < 2:
            if distance_col == 0:
                self.initial_edges.append((str((i*self.lenght)+j),str(((i+1)*self.lenght)+j),1))
            else:
                self.initial_edges.append((str((i*self.lenght)+j),str(((i+1)*self.lenght)+j),3))
                
    def distance_counter_line(self,i,j):
        if j < self.lenght-1:
            distance_line = abs(int(self.envi[i][j+1])-int(self.envi[i][j]))
            if distance_line < 2:
                if distance_line == 0:
                    self.initial_edges.append((str((i*self.lenght)+j),str(((i)*self.lenght)+j+1),1))
                else:
                    self.initial_edges.append((str((i*self.lenght)+j),str(((i)*self.lenght)+j+1),3))
 
    def tuple_maker(self):
        permission = "ok"
        for i in range(self.width-1):
            for j in range(self.lenght):
                if self.envi[i][j] == "$" or self.envi[i][j].upper() == "X":
                    self.initial_edges.append((str((i*self.lenght)+j),str(((i+1)*self.lenght)+j),2))
                    if j < self.lenght-1:
                        self.initial_edges.append((str((i*self.lenght)+j),str((i*self.lenght)+j+1),2))
                else:
                    if self.envi[i+1][j] == "$" or self.envi[i+1][j] == "X":
                        self.initial_edges.append((str((i*self.lenght)+j),str(((i+1)*self.lenght)+j),2))
                        permission = "no"
                    
                    if j < self.lenght-1 and (self.envi[i][j+1] == "$" or self.envi[i][j+1] == "X"):
                        self.initial_edges.append((str((i*self.lenght)+j),str(((i)*self.lenght)+j+1),2))
                        if permission != "no":
                            self.distance_counter_col(i,j)
                    else:
                        if permission != "no":
                            self.distance_counter_col(i,j)                      
                        self.distance_counter_line(i,j)
                permission = "ok"

    def dijsktra(self,initial, end):
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        
        while current_node != end:
            visited.add(current_node)
            destinations = self.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]
            
            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path

    def finding_sum(self,path):
        lenght = 0
        for i in range(len(path)-1):
            first_id = path[i]
            second_id = path[i+1]
            for para in self.initial_edges:
                if first_id == para[0] and second_id == para[1] or (first_id == para[1] and\
                   second_id == para[0]):
                    lenght += para[2]
        return lenght

    def make_all_combinations(self,a_list):
        all_combinations = []
        for r in range(len(a_list) + 1):
            combinations_object = itertools.combinations(a_list, r)
            combinations_list = list(combinations_object)
            all_combinations += combinations_list
        return all_combinations

    def making_iteration(self,a_list):
        a_list.sort()
        pomocne = self.numbers
        path_sum = 0
        mini=sys.maxsize
        all_combinations = self.make_all_combinations(a_list)
        for path in all_combinations:
            for i in range(len(list(path))):
                for j in range(len(a_list)):
                    if path[i] == a_list[j]:
                        a_list.pop(j)
                        break   
                    
            my_sum = sum(a_list[0:len(a_list)-1])*2
            if len(a_list):
                my_sum +=a_list[-1]

            if len(path):
                path_sum = (sum(path) - path[-1])*2+path[-1]
            
            if path_sum >= my_sum:
                if path_sum < mini:
                    mini = path_sum
            else:
                if my_sum<mini and my_sum>0:
                    mini = my_sum
            a_list = []
            for znak in pomocne:
                a_list.append(znak)
        return mini
                              
    def __str__(self):
        self.loading()
        return str(self.main_loop())

loop = input("loop: ").strip()
if len(loop)>= 1 and loop.isdigit():
    while int(loop)!=0:
        interface = input("interface: ").split()
        if len(interface)==2 and interface[1].isdigit() and interface[0].isdigit():
            print(Main(interface))
        else:
            print("Wrong input! One more time.")
            continue
        loop = int(loop)-1
else:
    print("Wrong input")
