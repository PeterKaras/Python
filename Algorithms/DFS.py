from collections import defaultdict 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v):
        #print(self.graph)
        self.graph[u].append(v)
        #print(self.graph)
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v,end = ' ')
        #print(v)
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]:
            #print(self.graph[v])
            #print(visited)
            if visited[i] == False:
                #print("visi",visited[i])
                self.DFSUtil(i, visited)
            #print("toto",visited[i])
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (max(self.graph)+2)
        #print(max(self.graph))
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited)
        #print(visited)
        

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 

g.DFS(2)
