# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  def DFS(root):
    if not root:
      return 0
    stack = [root]
    total = 0
    while stack:
      current = stack.pop()
      total+= current.val
      if current.left:
        stack.append(current.left)
      if current.right:
        stack.append(current.right)
    return total
  #return DFS(root)

  def DFS_recusrive(root):
    if root is None:
      return 0

    