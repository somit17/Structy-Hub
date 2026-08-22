def union(roots,sizes,node_a,node_b):
  root_a = find(roots,node_a)
  root_b = find(roots,node_b)

  if root_a == root_b:
    return
  
  if sizes[root_a] > sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a]+= sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b]+= sizes[root_a]

def find(roots,node):
  if roots[node] == node:
    return node
  found =  find(roots,roots[node])
  roots[node] = found
  return found
  
def count_components(n, edges):

  roots = [i for i in range(0,n)] #[0,1,2,3...n]

  sizes = [1 for i in range(0,n)]

  for edge in edges:
    node_a,node_b = edge
    union(roots,sizes,node_a,node_b)

  count = 0
  for i in range(0,n):
    if roots[i] == i:
      count+=1
  return count