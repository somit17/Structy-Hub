# binary search index

Write a function that takes in a sorted list of numbers and a target. The function
should return the index where the target can be found within the list. If the target is not found
in the list, then return the index where it should appear in the sorted order.

You may assume that the input list contains unique numbers sorted in increasing order.

Your solution should have a runtime of O(logn).

#### test_00

```python
binary_search_index([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
```

#### test_01

```python
binary_search_index([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> 8
```

#### test_02

```python
binary_search_index([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2
```

#### test_03

```python
binary_search_index([0, 6, 8, 12, 16, 19, 20, 28], 7) # -> 2
```

#### test_04

```python
binary_search_index([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) # -> 8
```

#### test_05

```python
binary_search_index([7, 9], 9) # -> 1
```

#### test_06

```python
binary_search_index([7, 9], 12) # -> 2
```

#### test_07

```python
binary_search_index([], 7) # -> 0
```
