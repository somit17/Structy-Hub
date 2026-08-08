# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):
    # DFS Iterative
    def dfs_iterative(root):
        if not root:
            return []
        stack = [(root, 0)]
        levels = []
        while stack:
            current, level_num = stack.pop()
            if len(levels) == level_num:
                levels.append([current.val])
            else:
                levels[level_num].append(current.val)
            
            # Push right first so left is processed first (LIFO)
            if current.right:
                stack.append((current.right, level_num + 1))
            if current.left:
                stack.append((current.left, level_num + 1))
        return levels
    
    # BFS Iterative
    def bfs_iterative(root):
        if not root:
            return []
        queue = deque([(root, 0)])  # Fixed: use () not []
        levels = []
        while queue:
            current, level_num = queue.popleft()
            if len(levels) == level_num:
                levels.append([current.val])
            else:
                levels[level_num].append(current.val)
            
            if current.left:    # BFS typically processes left then right
                queue.append((current.left, level_num + 1))
            if current.right:
                queue.append((current.right, level_num + 1))
        return levels
    
    # DFS Recursive helper
    def fill_levels(root, levels, level_num):
        if not root:
            return
        
        if len(levels) == level_num:
            levels.append([root.val])  # Fixed: use root.val, not current.val
        else:
            levels[level_num].append(root.val)  # Fixed: use root.val
        
        fill_levels(root.left, levels, level_num + 1)
        fill_levels(root.right, levels, level_num + 1)
    
    def dfs_recursive(root):
        levels = []
        fill_levels(root, levels, 0)
        return levels
    
   
    return dfs_recursive(root) 