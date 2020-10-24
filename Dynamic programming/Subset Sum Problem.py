class Main:
    def __init__(self,needed_sum,numbers):
        self.numbers = numbers
        self.need_sum = needed_sum
        self.matrix = [[int(numbers[0]) for i in range(len(numbers)+1)]
                       for j in range(len(numbers)+1)]

    def main_loop(self):            
        for i in range(len(self.numbers)):
            for j in range(i+1,len(self.numbers)+1):
                for k in range(j,len(self.numbers)):
                    print(int(self.numbers[j]))
                    self.matrix[j][k] = int(self.numbers[j-1]) + self.matrix[j-1][k]
                    if self.matrix[j][k] == self.need_sum:
                        return "True"
            print(self.matrix)

            self.matrix = [[int(self.numbers[i]) for k in range(len(numbers)+1)]
                       for m in range(len(numbers)+1)]
        return "False"
    
    def __str__(self):
        return self.main_loop()

def checking(numbers):
    for num in numbers:
        if num.isdigit():
            continue
        return "Revise"

loop = input("Loop: ").strip()
if len(loop)>=1 and loop.isdigit():
    while int(loop)!= 0:
        numbers = input("Numbers: ").split()
        if checking(numbers) != "Revise":
            needed_sum = input("Sum: ").strip()
            if len(needed_sum)>= 1 and needed_sum.isdigit():
                print(Main(int(needed_sum),numbers))
            else:
                print("Wrong input!")
                continue
            loop = int(loop)-1
        else:
            print("Wrong input!")
else:
    print("Wrong Input!")
