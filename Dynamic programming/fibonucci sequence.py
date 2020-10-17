class Main:
    def __init__(self,n):
        self.n = int(n)
        self.fibo = [0,1]

    def main_loop(self):
        for i in range(2,self.n+1):
            self.fibo.append(self.fibo[i-1] + self.fibo[i-2])

    def __str__(self):
        self.main_loop()
        print(self.fibo)
        return str(self.fibo[-1])

iteration = input("Iteration: ").strip()
if len(iteration)>= 1 and iteration.isdigit():
    print(Main(iteration))
else:
    print("Wrong Input!")

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(3))
