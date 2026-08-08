# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  #DFS
  def dfs(root,target):
    if not root:
      return False
    stack = [root]
    while stack:
      current = stack.pop()
      if current.val == target:
        return True
      if current.left:
        stack.push(current.left)
      if current.right:
        stack.push(current.right)
    return False
  return dfs(root,target)