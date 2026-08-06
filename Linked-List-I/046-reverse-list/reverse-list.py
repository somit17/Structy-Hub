# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  prev = None
  current = head
  while current :
    next = current.next
    current.next = prev
    prev = current
    current = next

  return prev

def recursive(head,prev = None):
  if head is None:
    return prev

  next = head.next
  head.next = prev
  return recursive(next,head)
