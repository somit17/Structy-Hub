def can_concat(s, words):
  return _can_concat(s,words,{})


def _can_concat(s, words,memo):
  if s in memo:
    return memo[s]
    
  if s == '':
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      memo[suffix] = _can_concat(suffix,words)
      if memo[suffix]:
        return True
        
  memo[s] = False
  return False 