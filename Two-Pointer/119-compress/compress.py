def compress(s):
  s+='!'
  result = []
  i,j = 0,0
  while j < len(s):
    if s[i] == s[j]:
      j+=1
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)+s[i])
      i=j

  return ''.join(result)