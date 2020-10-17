graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        print("v",vertex)
        print("S",stack)
        if vertex not in visited:
            #print("VERTEX",vertex)
            visited.add(vertex)
            print("VISITED",visited)
            stack.extend(graph[vertex] - visited)
            print("g",graph[vertex],visited)
            print("STACK",stack)
    return visited

print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}





"""def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']0]"""
