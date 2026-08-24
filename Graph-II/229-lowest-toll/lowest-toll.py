def lowest_toll(highway_tolls, start_city, end_city):
  graph = {}
  for highway in highway_tolls:
    src,dst,tax = highway
    if src not in graph: graph[src] = []

    if dst not in graph: graph[dst] = []

    graph[src].append((dst,tax))
    graph[dst].append((src,tax))
      

  return dfs(graph,start_city,end_city,set())
  #print(graph)


def dfs(graph,src,dst,visited):

  if src == dst:
    return 0

  if src in visited:
    return float('inf')

  visited.add(src)
  min_cost = float('inf')
  for dst_path in graph[src]:

    neighbor,tax = dst_path

    total= tax + dfs(graph,neighbor,dst,visited)
    min_cost = min(min_cost,tax)

  visited.remove(src)
  return min_cost
  