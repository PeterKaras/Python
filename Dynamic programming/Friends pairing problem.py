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
            print(countFriendsPairings(int(n)))
        else:
            print("Wrong Input!")
            continue
        loop = int(loop)-1
else:
    print("Wrong Input!")
