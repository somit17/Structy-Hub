def is_subsequence(string_1, string_2):

  s1 = 0
  s2 = 0
  while s1 < len(string_1) and s2 < len(string_2):
    if string_1[s1] == string_2[s2]:
      s1 +=1
      s2 +=1
    else:
      s2+=1
  return s1 == len(string_1)
    