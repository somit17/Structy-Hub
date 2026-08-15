def quickest_concat(s, words):
  result =  _quickest_concat(s, words,0,{})
  if result == float('inf'):
    return - 1
  else:
    return result


def _quickest_concat(s, words,idx,memo):

  if idx in memo:
    return memo[idx]

  if idx == len(s):
    return 0

  min_count = float('inf')
  for word in words:
    if s.startswith(word,idx):
      count = 1 + _quickest_concat(s,words,idx + len(word),memo)
      min_count = min(min_count,count)
     
  memo[idx] = min_count
  return min_count