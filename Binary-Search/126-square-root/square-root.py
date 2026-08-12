def square_root(n):
  L = 0
  H = n
  while L <= H:
    mid = (L + H) // 2
    sq = mid * mid 
    if sq == n:
      return mid
    elif sq > n:
      H = mid - 1
    else:
      L = mid + 1

  return H