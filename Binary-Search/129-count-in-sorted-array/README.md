# count in sorted array

Write a function that takes in a sorted list of numbers and a target as arguments. The function should return the number
of times the target element appears in the list.

Your solution should have a time complexity of O(logn).

#### test_00

```python
count_in_sorted_array([1,2,3,3,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 5
```

#### test_01

```python
count_in_sorted_array([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 4) # -> 1
```

#### test_02

```python
count_in_sorted_array([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 12) # -> 0
```

#### test_03

```python
count_in_sorted_array([2,2,5,7,8,8,10,10,10,12,15,18,20], 10) # -> 3
```

#### test_04

```python
count_in_sorted_array([42], 42) # -> 1
```

#### test_05

```python
count_in_sorted_array([], 42) # -> 0
```

#### test_06

```python
nums = [1] * 30000 # [1,1,1,...]
count_in_sorted_array(nums, 1) # -> 30000
```
