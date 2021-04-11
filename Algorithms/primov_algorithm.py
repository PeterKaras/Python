import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices
        print("SELF",self.V)
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.V): 
            print ("MSTT",parent[i], "-", i, "\t", self.graph[i][ parent[i] ] )
  
    def minKey(self, key, mstSet): 
        min = sys.maxsize
        print("KEY",key)
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False:
                print("KEYYYYYY",key[v])
                min = key[v] 
                min_index = v

        print(min_index)
        return min_index 
  
    def primMST(self): 
        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V
        parent[0] = -1 
  
        for cout in range(self.V): 
            print("PRED",key)
            u = self.minKey(key, mstSet) 
  
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent) 
  
g = Graph(4) 
g.graph = [ [0, 1, 1, 3], 
            [2, 0, 1, 2], 
            [2, 1, 0, 1], 
            [2, 2, 4, 0]] 
  
g.primMST(); 
