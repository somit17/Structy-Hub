def decompress_braces(string):
  number_chars = '123456789'
  stack = []

  for char in string:
    if char in number_chars:
      stack.append(int(char))
    else:
      if char == '}':
        #popping subroutine
        segment = ''
        while not isinstance(stack[-1],int):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
        
      elif char != '{':
          stack.append(char)

    return ''.join(stack)
