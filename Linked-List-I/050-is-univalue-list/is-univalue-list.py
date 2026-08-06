# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  if not head:
    return True
  current = head
  while current:
    if current.val != head.val:
      return False
    current = current.next
  return True

def recursive(head,prev_val = None):
  if head is None:
    return True

  if prev_val is None and head.val != prev_val:
    return False

  return recursive(head.next,head.val)
  