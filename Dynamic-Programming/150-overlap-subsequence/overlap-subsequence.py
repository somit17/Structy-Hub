def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2,0,0,{})

def _overlap_subsequence(string_1, string_2,start1,start2,memo):

  key = (start1,start2)
  if key in memo:
    return memo[key]
    
  if start1 == len(string_1) or start2 == len(string_2):
    return 0

  if string_1[start1]==string_2[start2]:
     memo[key] =  1 + _overlap_subsequence(string_1,string_2,start1 + 1,start2 + 1)
  else:
    memo[key] =  max(
    _overlap_subsequence(string_1,string_2,start1 + 1,start2),
    _overlap_subsequence(string_1,string_2,start1,start2 + 1)
    )

  return memo[key]
    
