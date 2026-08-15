def valid_compound(compound, elements):
  return _valid_compound(compound,elements,0,{})

def _valid_compound(compound, elements,idx,memo):
  if idx in memo:
    return memo[idx]

    
  if idx == len(compound):
    return True

  for element in elements:
    if compound.startswith(element.lower(),idx):
      if _valid_compound(compound,elements,idx + len(element),memo):
        memo[idx] = True
        return True
  memo[idx] = False
  return False