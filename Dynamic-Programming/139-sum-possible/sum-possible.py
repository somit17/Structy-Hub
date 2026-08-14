def sum_possible(amount, numbers):
  return _sum_possible(amount,numbers,{})
  
def _sum_possible(amount, numbers,memo):
  if amount in memo:
    return memo[amount]
    
  if amount == 0:
    return True

  if amount < 0:
    return 

  for idx in range(len(numbers)):
    remaining_amount = amount - numbers[idx]
    memo[remaining_amount] = _sum_possible(remaining_amount,numbers,memo)
    if memo[remaining_amount]:
      return True

  return False
