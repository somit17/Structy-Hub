# find leftmost index

Write a function that takes in a sorted list of numbers and a target as arguments. The function should return the
leftmost index where the target can be found in the list. If the target does not exist in the list, then return -1.

Your solution should have a time complexity of O(logn).

#### test_00

```python
find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 2
```

#### test_01

```python
find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 4) # -> 5
```

#### test_02

```python
find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 12) # -> -1
```

#### test_03

```python
find_leftmost_index([2,2,5,7,8,8,10,10,10,12,15,18,20], 10) # -> 6
```

#### test_04

```python
find_leftmost_index([42], 42) # -> 0
```

#### test_05

```python
find_leftmost_index([], 42) # -> -1
```

#### test_06

```python
nums = [1] * 30000 # [1,1,1,...]
find_leftmost_index(nums, 1) # -> 0
```
