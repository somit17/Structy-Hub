def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
    dfs(graph,node,distance)

  return max(distance.values())


  
def dfs(graph,node,distance):

  if node in distance:
    return distance[node]

  largest = 0
  for neighbor in graph[node]:
    attempt = dfs(graph,neighbor,distance)
    largest = max(attempt,largest)

  distance[node] = 1 + largest
  return distance[node]