def prereqs_possible(num_courses, prereqs):
  graph = build_graph(num_courses,prereqs)
  visiting = set()
  visited = set()
  print(graph)
  for start_node in range(0,num_courses):
    if detect_cycle(graph,start_node,visiting,visited):
      return False

  return True
  
def detect_cycle(graph,node,visiting,visited):

  if node in visited:
    return False

  if node in visiting:
    return True #Cycle detected

  visiting.add(node)
  
  for neighbor in graph[node]:
    if detect_cycle(graph,neighbor,visiting,visited):
      return True

  visiting.remove(node)
  visited.add(node)

  return False

def build_graph(num_courses,prereqs):
  graph = {}
  for i in range(0, num_courses):
    graph[i] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
    
  return graph

# numCourses = 6
# prereqs = [
#   (0, 1),
#   (2, 3),
#   (0, 2),
#   (1, 3),
#   (4, 5),
# ]
# prereqs_possible(numCourses, prereqs) # -> True