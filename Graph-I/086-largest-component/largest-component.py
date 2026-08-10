def largest_component(graph):
  visited = set()
  max_size = float('-inf')
  curr_size = 0
  for node in graph:
    curr_size = explore(graph,node,visited)
    max_size = max(max_size,curr_size)
  return max_size
  

def explore(graph,current_node,visited):

  if current_node in visited:
    return 0

  visited.add(current_node)
  size = 1
  for neighbor in graph[current_node]:
    size+=explore(graph,neighbor,visited)

  return size
  