class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  
  if index == 0:
    dummyNode = Node(value)
    dummyNode.next = head
    return dummyNode

  count = 0
  current = head
  while current:
    if count + 1 == index:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
    count+=1
    current = current.next
  return head

def insert_node_recursive(head, value, index,count = 0):
  if index == 0:
    dummyNode = Node(value)
    dummyNode.next = head
    return dummyNode
    
  if head is None:
    return None

  if count+1 == index:
    temp = head.next
    head.next = Node(value)
    head.next.next = temp
    return

  insert_node_recursive(head.next,value,index,count+1)
  return head
  
