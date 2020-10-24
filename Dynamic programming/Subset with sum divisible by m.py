def modularSum(arr, n, m): 
  
    if (n > m): 
        return True
    #will create list of m matrix with value False
    DP = [False for i in range(m)] 
  
    for i in range(n): 

        #It will return True value if index 0 of DP is True       
        if (DP[0]): 
            return True
        
        #
        temp = [False for i in range(m)] 
  
        for j in range(m): 
          
            if (DP[j] == True): 
              
                if (DP[(j + arr[i]) % m] == False): 

                    temp[(j + arr[i]) % m] = True
              
        for j in range(m): 
            if (temp[j]): 
                DP[j] = True
  
        DP[arr[i] % m] = True
      
    return DP[0] 

arr = [1, 7,8,8] 
n = len(arr) 
m = 5
print("YES") if(modularSum(arr, n, m)) else print("NO")
