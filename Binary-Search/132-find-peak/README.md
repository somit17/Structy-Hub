# find peak

Write a function that takes in a list of numbers. The function should return the index of a "peak" element. A "peak" is
an element that is greater than both of its adjacent neighbors. If there are multiple peaks, you may return the index of
any one of them.

Note that the first and last elements of the list only need to be greater than their single neighbor to be considered a
"peak".

Your solution should have a time complexity of O(logn).

You can assume that adjacent numbers of the list are not equal.

#### test_00

```python
find_peak([4,5,6,3,1]) # -> 2
# 6 is a peak b/c it is greater than both of its neighbors 
```

#### test_01

```python
find_peak([2,5,7,10,12]) # -> 4
# 12 is a peak b/c it is greater than its single neighbor
```

#### test_02

```python
find_peak([55,50,20,21,5,3,2]) # -> 0 or 3
```

#### test_03

```python
find_peak([6,8,9,12,10,9,7,8,4]) # -> 3 or 7
```

#### test_04

```python
find_peak([1,2,3,4,5,6,7,1,2,3,4,5,4]) # -> 6 or 11
```