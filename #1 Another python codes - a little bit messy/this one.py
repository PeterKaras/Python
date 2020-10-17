import turtle 
import math

def down_leaves(uhol,j,k,head,dlzka):
    for i in range(1,uhol):
        turtle.fd(dlzka)
        turtle.lt(1*k)
    turtle.setheading(head)
    if j == 1:
        return 0
    down_leaves(uhol,1,k,head,dlzka)

def stem(r,angle,sign):
    arc_lenght = 2*math.pi*r*angle/360
    n = int(arc_lenght/3)+1
    step_lenght = arc_lenght/n
    step_angle = angle/n
    for i in range(n):
        turtle.fd(step_lenght)
        turtle.rt(step_angle*sign)
        
def sepals(leaves,uhol,dlzka):
    angle_mid = 360/leaves
    turtle.setheading(0)
    for i in range(leaves):
        down_leaves(uhol,0,1,180+angle_mid*(i),dlzka)
        turtle.setheading(angle_mid*(i+1))
        
turtle.speed(50)
#[12,2,165,55],[7,30,2,170,55],[22,4,170,15]
leaves = int(input("leaves: "))
#uhol_listy = int(input("uhol na listy: "))
dlzka = int(input("Zadajte dlzku listov: "))
stonka = int(input("Zadajte dlzku stonky: "))
uhol_sepals = int(input("Uhol na sepals: "))

#na 1 a 3 kvetinu
stem(50,90,-1)
turtle.setheading(180)
stem(50,90,-1)
turtle.setheading(180)
stem(50,90,1)
turtle.setheading(0)
stem(50,90,1)

#na 2 kvetinu
"""turtle.setheading(uhol_listy)
down_leaves(uhol_listy+5,0,1,180+uhol_listy,4)
turtle.setheading(180-uhol_listy)
down_leaves(uhol_listy+5,0,-1,-uhol_listy,4)"""

turtle.setheading(135)

stem(stonka,90,1)

sepals(leaves,uhol_sepals,dlzka)
