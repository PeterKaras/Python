class Main:
    def __init__(self):
        self.old_field = ["XXX.X.X.XXXXXX.....X..X1...XXX...X.XXX..X1..X",
                          "..X.X.XX1.1X.X.XX.X...X1.X..X.XXX....XXXXX.X.",
                          "..X.XX.X.X.X..X.X.XX.1X11....X..XX......X.XX.",
                          "..XXX.XXXX.XX.XX.X.XXXXXXX.X..11...X.X.X.....",
                          "11..X11...XX....1X.X1.X...1X.XXX..XXX....XXX.",
                          "111..11....XXXX.1X.X.X.XX.1X..11....XX..X.X..",
                          "..1X.....XXX..111.X..XX.111X..11...X..XXX...X",
                          "XX.X...X...XXX.XXX.XXX...11.XXX...X..XX.XX.XX"]
        self.field = []
        self.width = 45
        self.height = 8
        self.result = 0

    def main_loop(self):
        self.field = [list(self.old_field[i]) for i in range(len(self.old_field))]
        k = 1
        p = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[p][j] == "1":
                    self.down_ending(p,j)
                    print("down")
                    for row in self.field:
                        print("".join(row))
                    print()
                if self.field[k][j] == "1":
                    print(k,j)
                    self.down_ending(k,j)
                    for row in self.field:
                        print("".join(row))
                    print()
            p +=2
            k += 2
            if p >=self.height or k>=self.height :
                break
        """k = len(self.field)-1
            for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == "1":
                    self.down_ending(i,j)
                if self.field[k][j] == "1":
                    self.up_ending(k,j)
            k -= 1
            if k <= i:
                break"""
        return self.result

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
                if i-k == -1:
                    return amount

    def right(self,i,j,word):
        amount = 0
        for k in range(self.width):
            if j+k >= self.width or self.field[i][j+k] == ".":
                #print(k,"som rzi")
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
            self.result += 1
        elif right_amount < down_amount:
            self.down(i,j,"Not")
            self.result += 1
        else:
            #self.right(i,j,"Not")
            self.down(i,j,"Not")
            self.result += 1
        print(self.result)

    def up_ending(self,i,j):
        print("som ru")
        right_amount = self.right(i,j,"Ok")
        up_amount = self.up(i,j,"Ok")
        if right_amount >= up_amount:
            self.right(i,j,"Not")
        else:
            self.up(i,j,"Not")
        self.result += 1
        print("ip",self.result)
    
    def __str__(self):
        return str(self.main_loop())

if __name__ == "__main__":
    print(Main())
