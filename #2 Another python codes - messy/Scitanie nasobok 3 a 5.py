nums = [3, 5]
maxI = 999

result = 0
for num in nums:
    for i in range(1,maxI):
        if num*i < maxI:
            result += num*i
            print(num,i)
print(result)


result = 0
for i in range(0,maxI):
    if i%3 == 0 or i%5 == 0:
        #print(i)
        result += i

print(result)




    







    
