# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  #DFS
  # def dfs(root,target):
  #   if not root:
  #     return False
  #   stack = [root]
  #   while stack:
  #     current = stack.pop()
  #     if current.val == target:
  #       return True
  #     if current.left:
  #       stack.append(current.left)
  #     if current.right:
  #       stack.append(current.right)
  #   return False
  # return dfs(root,target)


    def DFS_recusrive(root,target):
      if not root:
        return False
      if root.val == target:
        return True
      return DFS_recusrive(root.left,target) or DFS_recusrive(root.right,target)

    return DFS_recusrive(root,target)
      