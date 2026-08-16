def reverse_some_chars(s, chars):

  stack = []
  for ch in s:
    if ch in chars:
      stack.push(ch)

  #Stack - > a , e, o , a

  result = []

  for ch in s:
    if ch in chars:
      result.append(stack.pop())
    else:
      result.append(ch)

  return ''.join(result)