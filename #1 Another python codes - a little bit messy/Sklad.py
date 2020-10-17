import sys
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Main(Node):
    def __init__(self,range_field):
        self.range_field = range_field
        self.result = []
        self.mini= sys.maxsize
        self.central = None
        self.sklady = []
        
    def loading(self,field =[]):
        for i in range(int(self.range_field[0])):
            symbols = input("Zadajte vase znaky: ").strip()
            if self.checking(symbols,i) != "Prepracovat":
                field.append(list(symbols))
            else:
                return "Prepracovat"
        return field

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

    def astar(self,maze, start, end):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0
        open_list = []
        closed_list = []
        new_list= []
        open_list.append(start_node)

        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
                    
            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) \
                   or node_position[1] < 0:
                    continue

                if maze[current_node.position[0]][current_node.position[1]] == '$' or maze[node_position[0]][node_position[1]] == '$':
                    pass
                elif current_node.position == start:
                    pass
                elif abs(int(maze[node_position[0]][node_position[1]])-int(maze[current_node.position[0]][current_node.position[1]])) > 1:
                    continue

                new_node = Node(current_node, node_position)

                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)
            maze[current_node.position[0]][current_node.position[1]] = 12
            if current_node.position in new_list:
                return -1
            new_list.append(current_node.position)

    def creating_list(self,pole,equal=[],merge=""):
        #print(pole,"pPOEOPWQiqweopqwewenko")
        for i in range(len(pole)):
            for j in range(len(pole[0])):
                merge += str(pole[i][j])
            equal.append(list(merge))
            merge = ""
        return equal

    def finding_path(self):
        pass

    def hlavny_cyklus(self,field):
        #self.pokus = self.creating_list(field)
        self.central[0],self.central[1] = int(self.central[0]),int(self.central[1])
        start = tuple(self.central)
        field[self.central[0]][self.central[1]] = 0
        print("SELF",field)
        equal =  self.creating_list(field)
        print("EQUAL",equal)
        print()
        for end in self.sklady:
            end[0],end[1] = int(end[0]),int(end[1])
            end = tuple(end)
            path = self.astar(field, start , end)
            print("EQUAL",equal)
            print("FIELD",field)
            field = equal
            print("tototottoot",equal)
            print("field,",field)
            for position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                end_point = (end[0] + position[0], end[1] + position[1])
                if int(end_point[0]) < 0 or int(end_point[0]) >= len(field[0]) or int(end_point[1]) < 0 or \
                   int(end_point[1]) >= len(field[0]):
                    print()
                    pass
                else:
                    field[end_point[0]][end_point[1]] = 12
                    path = self.astar(field, start , end)
                    field = None
                
                    
                    #field = self.pokus[len(self.pokus)-3:len(self.pokus)]
        
            break


    def __str__(self):
        znak = self.loading()
        if znak != "Prepracovat":
            return str(self.hlavny_cyklus(znak))
        else:
            return "Prepracovat"
            
cyklus = input("Zadajte pocet cyklov: ").strip()
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
