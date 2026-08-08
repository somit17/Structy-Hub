# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if root is None:
    return -1

  if root.left is None and root.right is None:
    return 0

  left_height = how_high(root.left)
  right_height = how_high(root.left)
