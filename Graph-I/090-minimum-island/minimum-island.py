def minimum_island(grid):
  visited= set()
  result = float('inf')
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size =explore(grid,r,c,visited)
      if size > 0:
        result = min(result,size)
  return result


def explore(grid,r,c,visited):
  row_inbounds  = 0 <= r < len(grid)
  col_inbounds  = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return 0
    
  if grid[r][c] == 'W':
    return 0

  pos = (r,c)
  
  if pos in visited:
    return 0

  visited.add(pos)
  
  count = 1
  count+=explore(grid,r + 1,c,visited)
  count+=explore(grid,r - 1,c,visited)
  count+=explore(grid,r,c - 1,visited)
  count+=explore(grid,r,c + 1,visited)

  return count