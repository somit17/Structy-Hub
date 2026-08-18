def permutations(items):

  if len(items) == 0:
    return [ [] ]

  first = items[0] #a
  full_perm = []
  for perm in permutations(items[1:]): #[ [] ]
    for i in range(len(perm) + 1):
      full_perm.append(perm[:i] + [first] + perm[i:])

  return full_perm
