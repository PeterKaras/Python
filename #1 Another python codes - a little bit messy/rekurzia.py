import random
def move(hod,j=2):
    print(hod)
    if j+hod == 8:
        return 0
    move(random.randint(1,6))
    
move(random.randint(1,6))
