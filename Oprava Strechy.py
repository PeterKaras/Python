class Main:
    def __init__(self,range_of_field):
        self.width = int(range_of_field[1])
        self.height = int(range_of_field[0])
        self.field = []
        self.result = 0
        
    def loading(self):
        for i in range(self.height):
            row = input("Zadajte vase znaky: ").strip()
            if self.checking(row) != "Revise" and len(row) == self.width:
                self.field.append(list(row))
            else:
                return "Revise"
    
    def checking(self,row):
        for badge in row:
            if badge == "." or badge == "*":
                pass
            else:
                return "Revise"

    def main_loop(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == "*":
                    self.checking_positions(i,j)
                    print(self.result)
                    
                    for row in self.field:
                        print("".join(row))
                    print()

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == "1":
                    self.ending(i,j)
                    print(self.result)
                    for row in self.field:
                        print("".join(row))
                    print()
            
        for row in self.field:
            print("".join(row))
        print(self.result)
                    
    def checking_positions(self,i,j):
        amount=0
        k=0
        direction = []
        helpers = ["D","U","R","L"]
        permission = "Stop"
        #print(i,j)
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= y < self.width and 0 <= x < self.height and self.field[x][y] != ".":
                #print(x,y)
                amount += 1
                if amount <= 1 and permission == "Stop" and k<=1:
                    permission = "Ok"
                elif permission == "Ok" and amount >= 1 and k > 1:
                    self.field[i][j] = "1"
                    return 0
                direction.append(helpers[k])
            k += 1

        print("SDadadasdasdadas",direction)
        self.result += 1
        if len(direction) == 0:
            #self.result += 1
            self.field[i][j] = "X"
        else:
            self.writting(i,j,direction)
            
    def writting(self,i,j,direction):
        permi ="ok"
        spare = ""
        for znak in direction:
            if permi == "Nop" and znak == "L" and (spare == "U" or spare == "D"):
                continue
            if permi == "Nop" and znak == "R" and (spare == "U" or spare == "D"):
                continue
            if permi == "Nop" and znak == "D" and (spare == "R" or spare == "L"):
                continue
            if permi == "Nop" and znak == "U" and (spare == "R" or spare == "L"):
                continue
            
            if znak == "D":
                permi = self.down(i,j,"Not")
            elif znak == "U":
                permi = self.up(i,j)
            elif znak == "R":
                permi = self.right(i,j,"Not")
            else:
                permi = self.left(i,j)
            if permi == "Nop":
                spare = znak

    def down(self,i,j,word):
        amount = 0
        permission = "ok"
        for k in range(self.height):
            if i+k == self.height or self.field[i+k][j] == ".":
                if word == "Ok":
                    return amount
                return permission
            
            if self.field[i+k][j] == "*" and permission == "ok" and k!=0:
                permission = "Nop"
                
            if word == "Not":
                self.field[i+k][j] = "X"
                
            if word == "Ok":
                if self.field[i+k][j] == "1":
                    amount += 1
                if i+k == self.height-1:
                    return amount
            
    def up(self,i,j):
        permission = "ok"
        for k in range(self.height):
            if self.field[i-k][j] == "." or i-k == -1:
                return permission
            
            if self.field[i-k][j] == "*" and permission == "ok" and k!=0:
                permission = "Nop"
            
            self.field[i-k][j] = "X"

    def right(self,i,j,word):
        amount = 0
        permission = "ok"
        for k in range(self.width):
            if j+k == self.width or self.field[i][j+k] == ".":
                if word == "Ok":
                    return amount
                return permission
            
            if self.field[i][j+k] == "*" and permission == "ok" and k!=0:
                permission = "Nop"
                
            if word == "Not":
                self.field[i][j+k] = "X"
            if word == "Ok":
                if self.field[i][j+k] == "1":
                    amount += 1
                if j+k == self.width-1:
                    return amount

    def left(self,i,j):
        permission="ok"
        for k in range(self.width):
            if self.field[i][j-k] == "." or j-k == -1:
                return permission
            
            if self.field[i][j-k] == "*" and permission == "ok" and k !=0:
                permission = "Nop"

            self.field[i][j-k] = "X"

    def ending(self,i,j):
        right_amount = self.right(i,j,"Ok")
        down_amount = self.down(i,j,"Ok")
        if right_amount >= down_amount:
            self.right(i,j,"Not")
        else:
            self.down(i,j,"Not")
        self.result += 1
            
    def __str__(self):
        if self.loading() != "Revise":
            return str(self.main_loop())
        else:
            return "Revise"

loop = input("Zadajte pocet cyklov: ").strip()
if loop.isdigit() and len(loop)>= 1:
    while int(loop)>= 1:
        range_of_field = input("Zadajte rozmedzie pola: ").split()
        if len(range_of_field)== 2 and range_of_field[1].isdigit() and \
           range_of_field[0].isdigit():
            print(Main(range_of_field))
        else:
            print("Nezadali ste cislo!")
            continue
        loop = int(loop)-1
else:
    print("Nezadali ste cislo!")
