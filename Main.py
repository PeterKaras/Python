import numpy as np 
import matplotlib.pyplot as plt 
import time
import pandas as pd
import random
import copy

WIDTH = 40
LENGHT = 40
NUMBER_OF_OBJECTS = 30
    
class Grid:
    def __init__(self):
        self.town_pos = []
        self.pave_pos = []

    def intersection(self):
        for i in range(LENGHT+2):
            if i % 10 == 0:
                self.indexes_town(i)
                self.indexes_town(i+1)

    def indexes_town(self,i):
        for j in range(WIDTH+2):
            self.town_pos.append([i,j])
            self.town_pos.append([j,i])
   
    def indexes_pave(self,i):
        for j in range(LENGHT+2):
            self.pave_pos.append([i,j])
            self.pave_pos.append([j,i])

    def pavement_function(self):
        for pos in self.town_pos:
            if [pos[0]+1,pos[1]] not in self.town_pos and [pos[1],pos[0]+1] not in self.town_pos and pos[0] < LENGHT+1:
                self.pave_pos.append([pos[0]+1,pos[1]]) 
            elif [pos[0]-1,pos[1]] not in self.town_pos and [pos[1],pos[0]-1] not in self.town_pos and 0 < pos[0] < LENGHT+1:
                self.pave_pos.append([pos[0]-1,pos[1]]) 
        
class Humans_movement(Grid):
    def __init__(self,g):
        self.grid_obj = g
    
    def move_humans(self,position,direction,limit,cross,pos_human):  
        if list(position) in self.grid_obj.town_pos:
            cross = True
    
        while True:
            number = random.randint(0,10)
            if 0 <= number <= 7 or cross == True:
                temp_direction = direction
            elif 7 < number <= 8:
                temp_direction = self.change_direction(direction,"opposite")
            elif number > 8:
                temp_direction = self.change_direction(direction, "another")
              
            new_pos,command = self.decide_position_walk(position,temp_direction)
            
            if new_pos != False:
                if list(new_pos) in pos_human:
                    return position,direction,limit-1,cross,True
                if command == False:
                    cross = False
                return new_pos,temp_direction,limit-1,cross,False

    def change_direction(self,direction,word):
        if word == "opposite":
            if direction == "L":
                return "R"
            elif direction == "R":
                return "L"
            elif direction == "U":
                return "D"
            else:
                return "R"
        else:
            return random.choice("UDRL")
     
    def decide_position_walk(self,position,direction):
        if direction == "D":
            new_position = tuple([position[0],position[1]-self.get_distance_human()])
            new_position,command = self.side_check(new_position)
        elif direction == "U":
            new_position = tuple([position[0],position[1]+self.get_distance_human()])
            new_position,command = self.side_check(new_position)
        elif direction == "L":
            new_position = tuple([position[0]-self.get_distance_human(),position[1]])
            new_position,command = self.vertical_check(new_position)
        else:
            new_position = tuple([position[0]+self.get_distance_human(),position[1]])
            new_position,command = self.vertical_check(new_position)
        
        return new_position,command
    
    def get_distance_human(self):
        return int(random.choice("12"))
            
    def vertical_check(self,new_position):
        if 2 <= new_position[0] < LENGHT and (list(new_position) in self.grid_obj.town_pos or list(new_position) in self.grid_obj.pave_pos):
            command = self.compare(list(new_position))
            return new_position,command
        return False,False
    
    def side_check(self,new_position):
        if 2 <= new_position[1] < WIDTH and (list(new_position) in self.grid_obj.town_pos or list(new_position) in self.grid_obj.pave_pos):
            command = self.compare(list(new_position))
            return new_position,command
        return False,False

    def compare(self,pos):
        if pos in self.grid_obj.town_pos:
            return True
        return False
    
class Car_movement:
    def __init__(self,g,h):
        self.grid_obj = g
        self.human_obj = h
    
    #Auta v rohoch dokazu robit aj U turn 
    def move_cars(self,position,direction,limit,pos_car):
        while True:
            #lavy horny roh a dole 1 1 bod
            if (position[0] == 0 and position[1] == LENGHT+1) or (position[0] == 1 and position[1] == 1) or (position[0] == WIDTH and position[1] == LENGHT+1):
                #RIGHT
                temp_direction = "R"
            #ak je to v prvych dvoch stlpcoch a modulo 1 cislo idem doprava 
            elif (position[0] == 0 or position[0] == 1) and position[1] % 10 == 1:
                #RIGHT DECIDE
                temp_direction = self.change_direction(direction,"R")
            #dolny pravy roh a 40 40 bod 
            elif (position[0] == WIDTH+1 and position[1] == 0) or (position[0] == LENGHT and position[1] == WIDTH):
                #LEFT
                temp_direction = "L"
            #posledny stlpec a idem ked to modulo je 0 do riadku smerom vlavo
            elif (position[0] == WIDTH+1 or position[0] == WIDTH) and position[1] % 10 == 0:
                #LEFT DECIDE
                temp_direction = self.change_direction(direction,"L")
            #lavy dolny roh 
            elif (position[0] == 0 and position[1] == 0) or (position[0] == WIDTH and position[1] == 1):
                #UP
                temp_direction = "U"
            #prvy stlpec a modulo 0 ked pridem zlava a hore chcem ist 
            elif position[0] == 0 and position[1] % 10 == 0:
                #UP DECIDE
                temp_direction = self.change_direction(direction,"U")
            #pravy roh a lavy 1 40 bod
            elif (position[0] == LENGHT+1 and position[1] == WIDTH+1) or (position[0] == 1 and position[1] == LENGHT):
                #DOWN
                temp_direction = "D"       
            elif position[0] == 1 and position[1] % 10 == 1:
                 temp_direction = "D"    
            elif position[0] % 10 == 1 and (direction == "R" or direction == "L"):
                #DOWN DECIDE
                temp_direction = self.change_direction(direction,"D")
                
            elif position[0] % 10 == 1 and (direction == "R" or direction == "L"):
                #DOWN DECIDE
                temp_direction = self.change_direction(direction,"D")
            
            elif position[1] % 10 == 0 and (direction == "U" or direction == "D") and position[0] != 0:
                #LEFT DECIDE
                temp_direction = self.change_direction(direction,"L")

            elif position[1] % 10 == 1 and (direction == "U" or direction == "D") and position[0] != WIDTH:
                #RIGHT DECIDE
                temp_direction = self.change_direction(direction,"R")
                
            else:
                temp_direction = direction
                
            new_pos = self.decide_position_car(position,temp_direction)
            if new_pos != False:
                if list(new_pos) in pos_car or self.checking(new_pos,position) == True:
                    return position,direction,limit-1,True
                return new_pos,temp_direction,limit-1,False
    
    def checking(self,new_pos,old_pos):
        if new_pos[0] != old_pos[0]:
            my_range = abs(new_pos[0]-old_pos[0])
            if new_pos[0] > old_pos[0]:
                command = self.checking_humans_diag(my_range,1,old_pos[0],new_pos[1])
            else:
                command = self.checking_humans_diag(my_range,-1,old_pos[0],new_pos[1])
        else:
            my_range = abs(new_pos[1]-old_pos[1])
            if new_pos[1] > old_pos[1]:
                 command = self.checking_humans_verti(my_range,1,new_pos[0],old_pos[1])
            else:
                command = self.checking_humans_verti(my_range,-1,new_pos[0],old_pos[1])
        return command
                 
    def checking_humans_diag(self,my_range,sign,old_pos,new_pos):
        for i in range(1,my_range):
            if [old_pos+(i*sign),new_pos] in self.human_obj.pos_list_humans:
                #print("Zrazka")
                return True
        return False
    
    def checking_humans_verti(self,my_range,sign,new_pos,old_pos):
        for i in range(1,my_range):
            if [new_pos,old_pos+(i*sign)] in self.human_obj.pos_list_humans:
                #print("Zrazka")
                return True
        return False
        
    def change_direction(self,direction,possible):
        number = random.randint(0,100)
        if number <= 45:
            return direction
        return possible
    
    def decide_position_car(self,position,direction):
        if direction == "D":
            new_position = tuple([position[0],position[1]-self.get_distance_car()])
            new_position = self.side_check(new_position)
        elif direction == "U":
            new_position = tuple([position[0],position[1]+self.get_distance_car()])
            new_position = self.side_check(new_position)
        elif direction == "L":
            new_position = tuple([position[0]-self.get_distance_car(),position[1]])
            new_position = self.vertical_check(new_position)
        else:
            new_position = tuple([position[0]+self.get_distance_car(),position[1]])
            new_position = self.vertical_check(new_position)
        
        return new_position
    
    def get_distance_car(self):
        return int(random.choice("12345"))
    
    def vertical_check(self,new_position):
        if 0 <= new_position[0] <= LENGHT+2 and (list(new_position) in self.grid_obj.town_pos):
            return new_position
        return False
    
    def side_check(self,new_position):
        if 0 <= new_position[1] <= WIDTH+2 and (list(new_position) in self.grid_obj.town_pos):
            return new_position
        return False
    
class Humans:
    def __init__(self,g):
        self.pos_humans = {}
        self.pos_list_humans = []
        self.grid_class = g
        self.process_obj = Humans_movement(g)
        
    def random_people(self,NUMBER_OF_OBJECTS):
        number_of_people = random.randint(1,NUMBER_OF_OBJECTS)
        for i in range(number_of_people):
            numbers = np.random.choice(len(self.grid_class.pave_pos)-1)
            
            if self.grid_class.pave_pos[numbers] not in self.pos_list_humans:
                live_time = random.randint(1,3600)
                direction = random.choice("UDRL")
                self.pos_humans.update({tuple(self.grid_class.pave_pos[numbers]) : tuple([direction,live_time,False])})
                self.pos_list_humans.append(self.grid_class.pave_pos[numbers])
 
    def move(self):
        dic_humans = copy.deepcopy(self.pos_humans)
        for key in dic_humans:
            position, direction, limit, cross, command = self.process_obj.move_humans(key, dic_humans[key][0], dic_humans[key][1],dic_humans[key][2],self.pos_list_humans)
            if limit > 0:
                self.pos_humans.update({position:tuple([direction,limit,cross])})
                if command == False:
                    del self.pos_humans[key]
                    self.pos_list_humans.append(list(position))
                    self.pos_list_humans.remove(list(key))
            else:
                del self.pos_humans[key]
                self.pos_list_humans.remove(list(key))
                self.random_people(1)

class Cars:
    def __init__(self,g,h):
        self.pos_cars = {} 
        self.pos_list_cars = []
        self.grid_class = g
        self.human_obj = h
        self.process_obj = Car_movement(g,h)
         
    def random_cars(self,NUMBER_OF_OBJECTS):
        number_of_cars = random.randint(1,NUMBER_OF_OBJECTS)
        for i in range(number_of_cars):
            numbers = random.randint(1,len(self.grid_class.town_pos)-1)
          
            if self.grid_class.town_pos[numbers] not in self.pos_list_cars:
                live_time = random.randint(1,3600)
                direction = self.choose_direction(self.grid_class.town_pos[numbers])
                self.pos_cars.update({tuple(self.grid_class.town_pos[numbers]) : tuple([direction,live_time])})
                self.pos_list_cars.append(self.grid_class.town_pos[numbers])
                
    def choose_direction(self,position):
        if position[0] % 10 == 0:
            return "U"
        elif position[0] % 10 == 1:
            return "D"
        elif position[1] % 10 == 0:
            return "L"
        else:
            return "R"
                
    def move(self):
        dic_car = copy.deepcopy(self.pos_cars)
        for key in dic_car:
            position, direction, limit, command = self.process_obj.move_cars(key, dic_car[key][0], dic_car[key][1],self.pos_list_cars)
            
            if limit > 0:
                self.pos_cars.update({position:tuple([direction,limit])})
                if command == False:
                    del self.pos_cars[key]
                    self.pos_list_cars.append(list(position))
                    self.pos_list_cars.remove(list(key))
            else:
                del self.pos_cars[key]
                self.pos_list_cars.remove(list(key))
                self.random_cars(1)
       
def plotting(pos,pos1,cars,humans):
    humans = pd.DataFrame(humans)
    pos = pd.DataFrame(pos)
    pos1 = pd.DataFrame(pos1)
    cars = pd.DataFrame(cars)
    
    plt.scatter(pos1[1],pos1[0],color="r")
    plt.scatter(pos1[0],pos1[1],color="r")
    
    plt.scatter(pos[1],pos[0],color="b")
    plt.scatter(pos[0],pos[1],color="b")
    
    plt.scatter(cars[0],cars[1],color="pink")
    plt.scatter(humans[0],humans[1],color="y")
    plt.show()
    time.sleep(1)        

def main_loop():
    g = Grid()
    g.intersection()
    g.pavement_function()
    h = Humans(g)
    c = Cars(g,h)
    c.random_cars(NUMBER_OF_OBJECTS)
    h.random_people(NUMBER_OF_OBJECTS)

    for i in range(50):
        h.move()
        c.move()
        plotting(g.town_pos,g.pave_pos,c.pos_list_cars,h.pos_list_humans)

if __name__ == "__main__":
    main_loop()