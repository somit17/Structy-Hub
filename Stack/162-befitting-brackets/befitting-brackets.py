def befitting_brackets(string):
  map = {
    '{': '}',
    '[': ']',
    '(':')'
  }
  stack = []

  for ch in string:
    if ch in map:
      stack.append(map[ch])
    else:
      if stack and stack[-1]==ch:
          stack.pop()
      else:
        return False

  return len(stack)==0


  befitting_brackets('(){}[](())') # -> True
