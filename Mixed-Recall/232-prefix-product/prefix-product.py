def prefix_product(numbers):
  result = []
  product = 1
  for num in numbers:
    product*=num
    result.append(product)
  return result