def find_leftmost_index(nums, target):
  L = 0
  R = len(nums) - 1
  leftmost = -1
  while L <= R:
    mid = (L + R) // 2
    if nums[mid] == target:
      R = mid - 1
      leftmost = mid
    elif nums[mid] > target:
      R = mid - 1
    else:
      L = mid + 1

  return leftmost