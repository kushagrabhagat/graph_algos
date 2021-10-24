#indegree = an array indicating indegrees for each node
#neighbours = a HashMap recording neighbours of each node

def topo_sort():
  queue = []
  for i in indegree:
    if indegree[i] == 0:
      queue.append(i)
      
def bfs(node):
  while !queue.empty():
    node = queue.dequeue()
    for neighbour in neighbours[node]:
      indegree[neighbour] -= 1
      if indegree[neighbour] == 0:
        queue.append(neighbour)
