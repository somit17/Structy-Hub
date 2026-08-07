# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node_recursive(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node_recursive(head.next,target_val)
  return head
  
def remove_node(head, target_val):
  if head.val == target_val:
    return head.next
  current = head
  prev = None
  while current:
    if current.val == target_val:
      prev.next  = current.next
      break
    prev  = current
    current = current.next
    
  return head
