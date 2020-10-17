class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Main(Node):
    def __init__(self,essence):
        self.obstacles = int(essence[0])
        self.steps = int(essence[1])
        self.position_not = []

        
    def checking(self):
        for i in range(self.obstacles):
            position = input("Zadajte suradnice prekazky: ").split()
            if len(position) == 2 and position[0].replace("-","",1).isdigit() \
               and position[1].replace("-","",1).isdigit():
                self.position_not.append(position)
            else:
                return "Prepracovat"

    def astar(self,maze, start, end,bound=-1):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        closed_list = []

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

                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node,node_position)
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
                
            maze[current_node.position[0]][current_node.position[1]] = 1            
            end = (0,current_node.position[1])
            end_node = Node(None,end)
    
    def hlavny_cyklus(self):
        graph = self.creating_environment()
        start = (self.steps,self.steps)
        end = (0,self.steps)
        path = self.astar(graph, start, end)
        if path==None:
            return "0"
        elif self.steps-path[self.steps][0] >= 0:
            return self.steps-path[self.steps][0]
      

    def creating_environment(self):
        field = [[0 for i in range((self.steps*2)+1)]
                 for j in range((self.steps*2)+1)]

        for badge in self.position_not:
            if int(badge[0])<= 0:
                x_pos = (len(field[0])-1)-(self.steps-abs(int(badge[0])))
            else:
                x_pos = self.steps-abs(int(badge[0]))
                
            if int(badge[1]) >= 0:
                y_pos = self.steps-int(badge[1])
            else:
                y_pos = (len(field[0])-1)-(self.steps-abs(int((badge[1]))))
            field[x_pos][y_pos] = 1
        return field
    
    def __str__(self):
        if self.checking() != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return "Prepracovat"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>=1:
    while int(cyklus)!=0:
        essence = input("Zadajte pocet prekazok a krokov: ").split()
        if essence[0].isdigit() and essence[1].isdigit() and len(essence)==2:
            print(Main(essence))
        else:
            print("Nezadali ste cislo/a!")
            continue
        cyklus = int(cyklus)-1
else:
    print("Nezadali ste cislo!")















