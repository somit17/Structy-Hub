# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  if not head:
    return 0
  current = head
  total = 0
  while current:
    total+=current.val
    current = current.next
  return total
