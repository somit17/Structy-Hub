from collections import deque


def closest_carrot(grid, starting_row, starting_col):
  
  queue = deque([(starting_row,  starting_col,  0)])
  visited = set([ (starting_row, starting_col) ])
  while queue:
    r , c , distance = queue.popleft()

    if grid[r][c] == 'C':
      return distance
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for delta in deltas:
      delta_row , delta_col = delta
      neighbor_row = r + delta_row
      neighbor_col = c + delta_col

      pos = (neighbor_row,neighbor_col)
      
      row_inbounds =  0 <= neighbor_row < len(grid)
      col_inbounds =  0 <= neighbor_col < len(grid[0])

      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
        visited.add(pos)
        queue.append((neighbor_row,neighbor_col,distance + 1))
        
  return -1