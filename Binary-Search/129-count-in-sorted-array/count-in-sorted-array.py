def find_leftmost_index(nums, target):
  lo = 0
  hi = len(nums) - 1
  leftmost = -1
  while lo <= hi:
    mid = (hi + lo) // 2
    if target < nums[mid]:
      hi = mid - 1
    elif target > nums[mid]:
      lo = mid + 1
    else:
      hi = mid - 1
      leftmost = mid
  return leftmost

def find_rightmost_index(nums, target):
  lo = 0
  hi = len(nums) - 1
  rightmost = -1
  while lo <= hi:
    mid = (hi + lo) // 2
    if target < nums[mid]:
      hi = mid - 1
    elif target > nums[mid]:
      lo = mid + 1
    else:
      lo = mid + 1
      rightmost = mid
  return rightmost

def count_in_sorted_array(nums, target):
  right_index = find_rightmost_index(nums, target)
  left_index = find_leftmost_index(nums, target)
  if right_index == -1:
    return 0
  else:
    return right_index - left_index + 1
