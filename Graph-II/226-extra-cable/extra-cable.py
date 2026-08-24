def find(roots,node):
  if roots[node] == node:
    return node
  found = find(roots,roots[node])
  return found


def union(roots,sizes,node_a,node_b):
  root_a = find(roots,node_a)
  root_b = find(roots,node_b)

  if root_a == root_b:
    return False

  if sizes[root_a] > sizes[root_b]:
    roots[root_b] = roots[root_a]
    sizes[root_a] = sizes[root_b]
  else:
    roots[root_a] = roots[root_b]
    sizes[root_b] = sizes[root_a]

  return True


def extra_cable(num_computers, cables):

  sizes = [1 for i in range(0,num_computers)]
  roots = [i for i in range(0,num_computers)]

  for cable in cables:
    node_a,node_b = cable
    if union(roots,sizes,node_a,node_b) == False:
      return cable

    
  