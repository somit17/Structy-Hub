def paired_parentheses(s):

  map = {')':'('}
  stack = []
  for ch in s:
    if ch in map:
      if stack and len(stack) > 0:
        stack.pop()

    elif ch == '(':
      stack.append('(')
      
  return len(stack) == 0
