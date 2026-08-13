def find_in_rotated_sorted_array(nums, target):
  min_index = inclusive_point(nums)
  left_result = binary_search(nums,target,0,min_index - 1)
  right_result = binary_search(nums,target,min_index,len(nums) - 1)

  if left_result == -1:
    return right_result
  else:
    return left_result
  return -1
  
def inclusive_point(nums):
  L = 0
  R = len(nums) - 1
  while L < R:
    mid = (L + R) // 2
    if nums[mid] > nums[R]:
      L = mid + 1
    else:
      R = mid

  return L

def binary_search(nums,target,L,R):
  while L <= R:
    mid = (L + R) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      R = mid - 1
    else:
      L = mid + 1
  return -1

      