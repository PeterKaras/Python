from collections import defaultdict 
def printAllPathsUtil(graph,u, d, visited, path=[]):
    print(visited[u])
    if u == d: 
        print (path) 
    visited[u]= True
    path.append(u) 
  
    if u == d: 
        print (path) 
    else: 
        for i in graph[u]: 
            if visited[i]== False: 
                printAllPathsUtil(i, d, visited, path) 
                      
    path.pop() 
    visited[u]= False

def printAllPaths(V,graph ,s, d): 
    # Mark all the vertices as not visited 
    visited =[False]*(V)
    print(visited)
    printAllPathsUtil(graph,s, d, visited)
    
V = 4
graph = defaultdict(list)  
graph[0].append(1)
graph[0].append(2)
graph[0].append(3)
graph[2].append(0)
graph[2].append(1)
graph[1].append(3)
print(graph)
s = 2 ; d = 3
printAllPaths(V,graph,s, d) 
