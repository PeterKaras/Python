class Main:
    def __init__(self,budget):
        self.nums = int(budget[0])
        self.limit = int(budget[1])

    def loading(self):
        self.numbers = input("Numbers: ").split()
        if len(self.numbers) != self.nums and self.checking() == "Revise":
            self.loading()

    def checking(self):
        for num in self.numbers:
            if num.isdigit():
                continue
            return "Revise"

    def main_loop(self):
        sum_num,result = 0,0
        for number in sorted(self.numbers):
            sum_num += int(number)
            if sum_num <= self.limit:
                result += 1
            else:
                return result 
    
    def __str__(self):
        self.loading()
        return str(self.main_loop())


loop = input("Loop: ").strip()
if len(loop)>= 1 and loop.isdigit():
    while int(loop)!= 0:
        budget = input("N and B: ").split()
        if len(budget)==2 and budget[0].isdigit() and budget[1].isdigit():
            print(Main(budget))
        else:
            print("Wrong input")
            continue
        loop = int(loop)-1
else:
    print("Wrong input!")
