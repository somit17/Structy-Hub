# find in rotated sorted array

Write a function that takes in a list of sorted numbers that has been rotated a number of times, as well as a target element. The function should
return the index of the target in the list. If the target is not found in the list, then return -1.

Your solution should have a time complexity of O(logn).

You can assume that the input list contains unique elements.

#### test_00

```python
find_in_rotated_sorted_array([5,6,7,9,2,3,4], 7) # -> 2
# the original array was [2,3,4,5,6,7,9] and was rotated 4 times
```

#### test_01

```python
find_in_rotated_sorted_array([24,25,30,12,15,16,20,21,22,23], 16) # -> 5
```

#### test_02

```python
find_in_rotated_sorted_array([15,22,37,42,59,70,3,8], 42) # -> 3
```

#### test_03

```python
find_in_rotated_sorted_array([15,22,37,42,59,70,3,8], 45) # -> -1
```

#### test_04

```python
find_in_rotated_sorted_array([5,6,7,8,10], 5) # -> 0
```

#### test_05

```python
find_in_rotated_sorted_array([6,7,8,10,5], 5) # -> 4
```

#### test_06

```python
find_in_rotated_sorted_array([8, 2, 6], 3) # -> -1
```

#### test_07

```python
find_in_rotated_sorted_array([8, 2, 6], 8) # -> 0
```

#### test_08

```python
find_in_rotated_sorted_array([39,45,50,56,62,71,77,83,89,94,98,4,12,18,24,31], 45) # -> 1
```

#### test_09

```python
find_in_rotated_sorted_array([39,45,50,56,62,71,77,83,89,94,98,4,12,18,24,31], 18) # -> 13
```
