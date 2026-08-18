def create_combinations(items, k):

  #Base case 1 
  if len(items) < k:
    return []
  
  #Base case 2
  if k == 0:
    return [[]]

  first = items[0]
  partial_combos = create_combinations(items[1:],k - 1)

  combos_with_first = []

  for partial_combo in partial_combos:
    combos_with_first.append([first,*partial_combo])
  
  combos_without_first = create_combinations(items[1:],k)

  return combos_with_first + combos_without_first
    
  