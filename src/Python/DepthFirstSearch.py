# tradition implementation of dfs using adjacency list as dictionary 
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['E'],
    'D' : [],
    'E' : ['A'],
   
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'B')
