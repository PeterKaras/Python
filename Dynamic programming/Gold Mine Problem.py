class Main:
    def __init__(self,interface):
        self.width = int(interface[1])
        self.length = int(interface[0])
        self.matrix = []
        self.values = [[0 for i in range(self.length)]
                        for j in range(self.width)]

    #Input should be separated by spaces
    def loading(self):
        amount = self.length
        while amount != 0:
            row = input("Your input: ").split(" ")
            if len(row) == self.width and self.checking(row)!= "Revise":
                self.matrix.append(row)
            else:
                print("Wrong Input!")
                continue
            amount -= 1

    def checking(self,row):
        for letter in row:
            if letter.isdigit() or letter == ",":
                continue
            return "Revise"

    def comparing(self,values,k,j):
        if values > self.values[k][j]:
            self.values[k][j] = values
        if values > self.maximum:
            self.maximum = values

    def main_loop(self):
        self.maximum = -1
        for i in range(self.length):
            self.values[i][0] = self.matrix[i][0]
            for j in range(1,self.width):
                for k in range(self.length):
                    if k-1 < 0 or self.values[k-1][j-1] == 0:
                        pass
                    else:
                        values = int(self.values[k-1][j-1]) + int(self.matrix[k][j])
                        self.comparing(values,k,j)
                    
                    if k+1 >=self.length or self.values[k+1][j-1] == 0:
                        pass
                    else:
                        values = int(self.values[k+1][j-1]) + int(self.matrix[k][j])
                        self.comparing(values,k,j)
                        
                    if self.values[k][j-1] == 0:
                        pass
                    else:
                        values = int(self.values[k][j-1]) + int(self.matrix[k][j])
                        self.comparing(values,k,j)

            self.values = [[0 for i in range(self.length)]
                        for j in range(self.width)]
        return self.maximum
                
    def __str__(self):
        self.loading()
        return str(self.main_loop())

loop = input("Loop: ").strip()
if len(loop)>=1 and loop.isdigit():
    while int(loop)!=0:
        interface = input("Interface: ").split()
        if len(interface)==2 and interface[1].isdigit() and interface[0].isdigit():
            print(Main(interface))
        else:
            print("Wrong input!")
            continue
        loop = int(loop)-1
else:
    print("Wrong input!")
