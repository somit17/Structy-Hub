class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  dummy_head = Node(0)
  current = dummy_head
  current_1 = head_1
  current_2 = head_2
  while current_1 and current_2:
    if current_1.val < current_2.val:
      current.next = current_1
      current_1  = current_1.next
    else:
      current.next = current_2
      current_2 = current_2.next
    current = current.next

  if current_1:
    current.next  = current_1
  if current_2:
    current.next = current_2
  return dummy_head.next
