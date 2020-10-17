class Main:
    def __init__(self,range_of_field):
        self.width = int(range_of_field[1])
        self.height = int(range_of_field[0])
        self.field = []
        self.result = 0

    def loading(self):
        amount = self.height
        while amount != 0:
            row = input("Zadajte vase znaky: ").strip()
            if self.checking(row) != "Revise" and len(row) == self.width:
                self.field.append(list(row))
            else:
                print("WRONG INPUT!")
                continue
            amount -= 1
    
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

        k = 1
        p = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[p][j] == "1":
                    self.down_ending(p,j)    
                if self.field[k][j] == "1":
                    self.down_ending(k,j)
            p +=2
            k += 2
            if p >=self.height or k>=self.height :
                break
        print(self.result)

    def checking_positions(self,i,j):
        k = 0
        permission = "Stop"
        direction = []
        helpers = ["D","U","R","L"]
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= y < self.width and 0 <= x < self.height and self.field[x][y] != ".":
                if x != i and permission == "Stop":
                    permission = "Ok"
                elif j != y and permission == "Ok":
                    self.field[i][j] = "1"
                    return 0
                direction.append(helpers[k])
            k += 1
        self.result += 1
        if len(direction) == 0:
            self.field[i][j] = "X"
        else:
            self.writting(i,j,direction)

    def writting(self,i,j,direction):
        for znak in direction:
            if znak == "D":
                self.down(i,j,"Not")
            elif znak == "U":
                self.up(i,j,"Not")
            elif znak == "R":
                self.right(i,j,"Not")
            else:
                self.left(i,j)

    def down(self,i,j,word):
        amount = 0
        for k in range(self.height):
            if i+k >= self.height or self.field[i+k][j] == ".":
                if word == "Ok":
                    return amount
                return 0
                
            if word == "Not":
                self.field[i+k][j] = "X"
                
            if word == "Ok":
                if self.field[i+k][j] == "1":
                    amount += 1
                if i+k == self.height-1:
                    return amount
            
    def up(self,i,j,word):
        amount = 0
        for k in range(self.height):
            if self.field[i-k][j] == "." or i-k == -1:
                if word == "Ok":
                    return amount
                return 0
            if word == "Not":
                self.field[i-k][j] = "X"

            if word == "Ok":
                if self.field[i-k][j] == "1":
                    amount += 1
                if i-k == 0:
                    return amount

    def right(self,i,j,word):
        amount = 0
        for k in range(self.width):
            if j+k >= self.width or self.field[i][j+k] == ".":
                if word == "Ok":
                    return amount
                return 0
                
            if word == "Not":
                self.field[i][j+k] = "X"
                
            if word == "Ok":
                if self.field[i][j+k] == "1":
                    amount += 1
                if j+k == self.width-1:
                    return amount

    def left(self,i,j):
        for k in range(self.width):
            if self.field[i][j-k] == "." or j-k == -1:
                return 0
            self.field[i][j-k] = "X"

    def down_ending(self,i,j):
        right_amount = self.right(i,j,"Ok")
        down_amount = self.down(i,j,"Ok")
        if right_amount > down_amount:
            self.right(i,j,"Not")
        elif right_amount < down_amount:
            self.down(i,j,"Not")
        else:
            self.down(i,j,"Not")
        self.result += 1
        print(self.result)
        
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
