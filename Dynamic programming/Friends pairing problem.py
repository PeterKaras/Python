import itertools

def pairing(a_list):
    all_combinations = []
    for r in range(1):
        combinations_object = itertools.combinations(a_list,2)
        all_combinations += combinations_object
    return len(all_combinations)+1

def countFriendsPairings(n): 
    dp = [0 for i in range(n + 1)] 
    for i in range(n + 1): 
  
        if(i <= 2): 
            dp[i] = i 
        else: 
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2] 
    print(dp)
    return dp[n] 
    
loop = input("Loop: ").strip()
if len(loop)>= 1 and loop.isdigit():
    while int(loop)!= 0:
        n = input("Number of friends: ").strip()
        if len(n)>= 1 and n.isdigit():
            a_list = list(range(1,int(n)+1))
            print(pairing(a_list))
        else:
            print("Wrong Input!")
            continue
        loop = int(loop)-1
else:
    print("Wrong Input!")
            
#Another way to solve it 
n = 4
print(countFriendsPairings(n))
