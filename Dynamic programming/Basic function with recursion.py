import math
def sucet_f(n):
    if n == 0:
        return 0
    else:
        rec = sucet_f(n-1)
        num = int(input("Number: "))
        sucet = num+rec
        return sucet

def even_numbers(n):
    if n == 0:
        return 0
    else:
        res = even_numbers(n-1)
        cislo = int(input("Number: "))
        if cislo%2==0:
            return res+1
        return 0

def max_num(n):
    if n == 0:
        return 0
    else:
        res = max_num(n-1)
        number = int(input("Number: "))
        if number > res:
            return number
        return res

def sucet_even(n):
    if n == 0:
        return 0
    else:
        res = sucet_even(n-1)
        number = int(input("Number: "))
        if (res+number)%2 ==0:
            print("True")
            return number
        print("False")
        return number

def prime_number_inak(num):
    for j in range(2,int(math.sqrt(num))+1):
        if num%j == 0:
            return True
    return False

def prime_recursion(n):
    if n == 0:
        return 0
    else:
        res = prime_recursion(n-1)
        if prime_number_inak(n) == False:
            return res + 1
        return res
    
#print(sucet_f(3))
#print(even_numbers(3),)
#print(max_num(5))
#print(sucet_even(3))
print(prime_recursion(8))







