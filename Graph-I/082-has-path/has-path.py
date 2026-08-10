from collections import deque
# def has_path(graph, src, dst):
#   if src == dst:
#     return True

#   for neighbor in graph[src]:
#     if has_path(graph,neighbor,dst):
#       return True

#   return False

def has_path(graph, src, dst):
  queue = deque([src])
  while queue:
    current_node = queue.popleft()
    if current_node == dst:
      return True

    for neighbor in graph[current_node]:
      queue.append(neighbor)

  return False

#TC -> O(e) and SC -> O(n)