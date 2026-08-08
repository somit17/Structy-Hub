# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  if not root:
    return float('inf')
  
  left = min(tree_min_value(root.left))
  right = min(tree_min_value(root.right))

  return min(root.val,left,right)
  
                           