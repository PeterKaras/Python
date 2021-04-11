graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs_path(graph,start,end):
    result = []
    znak = dfs(graph,start,end,[],result)
    print(znak)
    return znak

def dfs(graph,start,end,path,result,i=0):
    path+=[start]
    if "A" in graph[start]:
        print("yeah")
        return "ok"
    if start == end and i != 0:
        result.append(path)
    else:
        for node in graph[start]:
            if node not in path:
                dfs(graph,node,end,path[:],result)
print(dfs_path(graph,'A','A')) 
