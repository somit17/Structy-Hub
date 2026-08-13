# min in rotated sorted array

Write a function that takes in a list of sorted numbers that has been rotated a number of times. The function should
return the minimum element of the list.

Your solution should have a time complexity of O(logn).

You can assume that the numbers of the input list are unique.

#### test_00

```python
min_in_rotated_sorted_array([6,7,9,10,2,3,4,5]) # -> 2
# the original array was [2,3,4,5,6,7,9,10] and was rotated 4 times
```

#### test_01

```python
min_in_rotated_sorted_array([24,25,30,12,15,16,20,21,23]) # -> 12
```


#### test_02

```python
min_in_rotated_sorted_array([15,22,37,42,59,70,3,8]) # -> 3
```

#### test_03

```python
min_in_rotated_sorted_array([5,6,7,8,9]) # -> 5
```

#### test_04

```python
min_in_rotated_sorted_array([5,6,7,8,4]) # -> 4
```

#### test_05

```python
min_in_rotated_sorted_array([39,45,50,56,62,71,77,83,89,94,98,4,12,18,24,31]) # -> 4
```