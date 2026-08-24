def weighted_graph_min_path(graph, src, dst):

  return min_path(graph,src,dst,set())

def min_path(graph,src,dst,visited):
  if src == dst:
    return 0

  if src in visited:
    return float('inf')

  visited.add(src)

  min_cost = float('inf')
  
  for neighbor in graph[src]:
    cost  = graph[src][neighbor]
    total_cost = cost + min_path(graph,neighbor,dst,visited)
    min_cost = min(min_cost,total_cost)

  visited.remove(src)

  return min_cost