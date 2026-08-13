def search_sorted_grid(grid, target):
  row = find_row(grid,target)
  if row == -1:
    return False
  else:
    return binary_search(grid,target,row)

  
def binary_search(grid,target,row):
   L = 0
   R = len(grid[0]) - 1
   while L <= R:
     mid = (L + R) // 2
     if grid[row][mid]==target:
       return True
     elif grid[row][mid] > target:
       R = mid - 1
     else:
       L = mid + 1
    return False

def find_row(grid,target):
  L = 0
  R  = len(grid) - 1
  while L <= R:
    mid = (L + R ) // 2
    if grid[mid][0] <= target <= grid[mid][-1]:
      return mid
    elif grid[mid][0] > target:
      R = mid - 1
    else:
      L = mid + 1

  return -1
  