def bellNumber(n): 
  
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1): 
  
        # Explicitly fill for j = 0 
        bell[i][0] = bell[i-1][i-1]
        print(bell)
  
        # Fill for remaining values of j 
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 
  
    return bell[n][0] 

for n in range(6): 
    print('Bell Number', n, 'is', bellNumber(n))

"""Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. """
"""
1
1  2
2  3  5
5  7  10 15
15 20 27 37 52
"""
