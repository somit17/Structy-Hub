from collections import Counter
def count_substring_at_most_k_distinct(s, k):
  window_map = Counter()
  start = 0
  count = 0

  for end in range(len(s)):
    leading_char = s[end]
    window_map[leading_char] = window_map.get(leading_char,0) + 1

    while len(window_map) > k : 
      trailing_char = s[start]
      window_map[trailing_char]-= 1
      if window_map[trailing_char] == 0 :
        del window_map[trailing_char]
      start+=1

    count += end - start + 1
  return count
        