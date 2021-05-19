import os 
import math

path = os.getcwd()
os.chdir(path)

def sumSubsets(numbers,n,target = 0):
    x = [0]*len(numbers)
    j = len(numbers) - 1 
  
    # Convert the array into binary array 
    while (n > 0):
      
        x[j] = n % 2 
        n = n // 2 
        j -= 1 
      
    sum_of_numbers = -1
  
    # Calculate the sum of this subset 
    for i in range(len(numbers)) :
        if (x[i] == 1) :
            sum_of_numbers += int(numbers[i]) 
    
            if sum_of_numbers+1 == target:
                with open("output_file1.txt","a") as f:
                    f.write("yes\n")
                    return True

def findSubsets(numbers, num_of_nums) :
  
    x = pow(2, len(numbers))
    for i in range(1, x) :
        out = sumSubsets(numbers, i)
        if out == True:
            return
    
    with open("output_file1.txt","a") as f:
        f.write("no\n")

def main_loop(file):
    for i in range(1,len(file)-1,2):
        num_of_nums = file[i]
        numbers = file[i+1].split(" ")
        if "0" in numbers:
            with open("output_file1.txt","a") as f:
                f.write("yes\n")
                continue
        findSubsets(numbers, num_of_nums)
        
def read_file():
    with open("test.in","r") as f:
        return f.read().split("\n")
               
if __name__ == "__main__":
    file = read_file()
    main_loop(file)