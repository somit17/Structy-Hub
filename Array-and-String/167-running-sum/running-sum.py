def running_sum(numbers):
  sum = 0
  for num in numbers:
    sum+=num
  result = [0] * (len(numbers) + 1)
  numbers.append(0)
  for i in range(len(numbers) - 1,-1,-1):
    print(f'numbers[i] --- > {numbers[i]}')
    sum-= numbers[i]
    result[i] = sum

  print(result)
    