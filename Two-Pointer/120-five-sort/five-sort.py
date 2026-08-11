def five_sort(nums):
  start = 0
  end = len(nums) - 1
  while start < end:
    if nums[start] == 5:
      nums[start],nums[end] = nums[end],nums[start]
      end-=1
    elif nums[end] == 5:
      end -=1
    else:
      start+=1

  return nums