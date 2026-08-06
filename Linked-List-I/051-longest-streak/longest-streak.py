# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  max_streak = 0
  current_streak = 0
  current = head
  prev_val = None
  while current:
    if prev_val == current.val:
      current_streak+=1
    else:
      current_streak = 1
    prev_val = current.val
    max_streak = max(max_streak,current_streak)
    current = current.next
    
  return max_streak

def longest_streak_recursive(head,prev_val = None):
  if head is None:
    return 0

  if head.val == prev_val:
    return 1

  
