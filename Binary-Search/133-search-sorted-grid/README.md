# search sorted grid

Write a function that takes in a grid of numbers and a target element as input. The function should return a boolean
indicating whether or not the target is present in the grid. Each row of the grid is sorted in increasing order. The
first element of each row is greater than the last element of the previous row.

Your solution should have a time complexity of O(log(m\*n)), where m is the number of rows and n is the number of
columns in the grid.

#### test_00

```python
grid = [
  [2,3,4,5],
  [11,12,12,15],
  [17,20,23,25],
  [30,31,32,50],
]
search_sorted_grid(grid, 12) # -> True
```

#### test_01

```python
grid = [
  [2,3,4,5],
  [11,12,12,15],
  [17,20,23,25],
  [30,31,32,50],
]
search_sorted_grid(grid, 21) # -> False
```

#### test_02

```python
grid = [
  [2,3,4,5],
  [11,12,12,15],
  [17,20,23,25],
  [30,31,32,50],
]
search_sorted_grid(grid, 55) # -> False
```

#### test_03

```python
grid = [
  [12,13,20,22,24],
  [26,27,29,30,33],
  [36,40,45,46,48],
  [54,55,60,67,70],
  [71,72,74,76,79],
  [85,87,90,92,98],
]
search_sorted_grid(grid, 87) # -> True
```

#### test_04

```python
grid = [
  [12,13,20,22,24],
  [26,27,29,30,33],
  [36,40,45,46,48],
  [54,55,60,67,70],
  [71,72,74,76,79],
  [85,87,90,92,98],
]
search_sorted_grid(grid, 71) # -> True
```

#### test_05

```python
grid = [
  [12,13,20,22,24],
  [26,27,29,30,33],
  [36,40,45,46,48],
  [54,55,60,67,70],
  [71,72,74,76,79],
  [85,87,90,92,98],
]
search_sorted_grid(grid, 25) # -> False
```

#### test_06

```python
grid = [
  [12,13,20,22,24],
  [26,27,29,30,33],
  [36,40,45,46,48],
  [54,55,60,67,70],
  [71,72,74,76,79],
  [85,87,90,92,98],
]
search_sorted_grid(grid, 10) # -> False
```

#### test_07

```python
grid = [
  [0,5,7],
]
search_sorted_grid(grid, 7) # -> True
```
