## count substring exactly k distinct

Write a function that takes in a string and a number k. The function should return the number of substrings that consist
of exactly k distinct characters.

#### test_00:

```python
count_substring_exactly_k_distinct("gattc", 3) # -> 3
# there are 3 substrings that consist of 3 distinct chars:
#  gat
#  gatt
#  attc   
```

#### test_01:

```python
count_substring_exactly_k_distinct("abacd", 3) # -> 3
```

#### test_02:

```python
count_substring_exactly_k_distinct("racetracks", 4) # -> 7
```

#### test_03:

```python
count_substring_exactly_k_distinct("pqpqs", 2) # -> 7
```

#### test_04:

```python
count_substring_exactly_k_distinct("aabacbebebe", 3) # -> 12
```

#### test_05:

```python
count_substring_exactly_k_distinct("serenenethers", 4); # -> 17
```
