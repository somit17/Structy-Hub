def min_in_rotated_sorted_array(nums):
  L = 0
  R = len(nums) - 1
  while L < R:
    mid = (L + R) // 2
    min_element = min(min_element,nums[mid])
    if nums[mid] > nums[R]:
      L = mid + 1
    else:
      R = mid
  return nums[L]   