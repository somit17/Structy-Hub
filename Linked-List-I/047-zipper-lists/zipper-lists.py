class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  dummyNode = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 and current_2:
    if count % 2 == 0:
      dummyNode.next = current_2
      current_2 = current_2.next
    else:
      dummyNode.next = current_1
      current_1 = current_1.next
    count+=1
    dummyNode = dummyNode.next

  if current_1:
    dummyNode.next = current_1
  if current_2:
    dummyNode.next = current_2
  return head_1
      
    
  pass # todo
