class Main:
    def __init__(self,number):
        self.number = number

    def maxDivider(self,i,delimer):
        while i%delimer==0:
            i //= delimer
        return i

    def main_loop(self,i):
        i = self.maxDivider(i,2)
        i = self.maxDivider(i,3)
        i = self.maxDivider(i,5)
        return "Yes" if i == 1 else "No"

    def GetUglyNumber(self):
        counter = 0
        i = 1
        while True:
            if self.main_loop(int(i)) == "Yes":
                counter += 1
            if counter == self.number:
                return i
            i += 1
        
    def __str__(self):
        return str(self.GetUglyNumber())


loop = input("Loop: ").strip()
if len(loop)>= 1 and loop.isdigit():
    while int(loop)!=0:
        number = input("Number: ").strip()
        if len(number)>=1 and number.isdigit():
            print(Main(int(number)))
        else:
            print("Wrong input!")
            continue
        loop = int(loop)-1
else:
    print("Wrong input!")
