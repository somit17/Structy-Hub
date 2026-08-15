def max_palin_subsequence(string):

  return _max_palin_subsequence(string,0,len(string) - 1,{})



def _max_palin_subsequence(string,start,end,memo):

  pos = (start,end)
  if pos in memo:
    return memo[pos]
  
  if start == end:
    return 1

  if start > end:
    return 0

  if string[start] == string[end]:
    return 2 + _max_palin_subsequence(string,start + 1,end - 1,memo)
  else:
    return max(
      _max_palin_subsequence(string,start + 1,end,memo),
      _max_palin_subsequence(string,start,end - 1,memo) 
      )
