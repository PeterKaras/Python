graph = {
  'A' : ['B','C'],
  'B' : ['D', ],
  'C' : [],
  'D' : [],
  'E' : [],
  'F' : ["E"]
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print("s",s,queue)
    print (s, end = "\n") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
    print(visited,queue)

# Driver Code
bfs(visited, graph, 'A')
