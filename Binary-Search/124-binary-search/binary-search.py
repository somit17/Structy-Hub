def binary_search(numbers, target):
  L = 0
  R = len(numbers) - 1
  while L <= R:
    mid = (L + R) // 2
    if numbers[mid] == target:
      return mid
    elif target > numbers[mid]:
      L = mid + 1
    else:
      R = mid - 1

  return -1