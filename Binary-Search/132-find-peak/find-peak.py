def find_peak(nums):
  L = 0
  R = len(nums) - 1
  while L < R:
    mid = (L + R) // 2
    if nums[mid] > nums[mid + 1]:
      R = mid
    else:
      L = mid + 1
  return L