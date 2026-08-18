def possible_paths(graph, src, dst):
  paths = dfs(graph, src, dst)
  return [ p[::-1] for p in paths ]


def dfs(graph,node,dst):
  if node == dst:
    return [ [node] ]

  paths = []
  for neighbor in graph[node]:
    neighbor_paths = dfs(graph,neighbor,dst)
    for neighbor_path in neighbor_paths:
      neighbor_path.append(node)
      paths.append(neighbor_path)
  return paths
    