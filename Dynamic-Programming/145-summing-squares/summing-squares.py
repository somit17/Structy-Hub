import math

def summing_squares(n):
  return _summing_squares(n,{})
  
def _summing_squares(n,memo):
  if n in memo:
    return memo[n]
    
  if n == 0:
    return 0

  min_sq = float('inf')
  
  for i in range(1,math.floor(math.sqrt(n)) + 1):
    sq = i * i
    curr_sq = 1 + _summing_squares(n - sq,memo)
    min_sq = min(min_sq,curr_sq)

  memo[n] = min_sq  
  return min_sq