matrix =    [["A","B","C","D"],
            ["E","F","G","H"],
            ["I","J","K","L"],
            ["M","N","O","P"]]
N = 4
result = [[matrix[y-x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]
print(result)
