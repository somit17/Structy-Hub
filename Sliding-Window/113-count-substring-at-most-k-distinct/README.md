## count substring at most k distinct

Write a function that takes in a string and a number k. The function should return the number of substrings that consist
of at most k distinct characters.

#### test_00:

```python
count_substring_at_most_k_distinct("gattc", 3) # -> 14
# there are 14 substrings that consist of at most 3 distinct chars:
#   gatt
#   attc
#   gat
#   att
#   ttc
#   ga
#   at
#   tt
#   tc
#   g
#   a
#   t
#   t
#   c
```

#### test_01:

```python
count_substring_at_most_k_distinct("gattc", 2) # -> 11
```

#### test_02:

```python
count_substring_at_most_k_distinct("abacd", 3) # -> 13
```

#### test_03:

```python
count_substring_at_most_k_distinct("abacd", 2) # -> 10
```

#### test_04:

```python
count_substring_at_most_k_distinct("racetracks", 4) # -> 34
```

#### test_05:

```python
count_substring_at_most_k_distinct("racetracks", 3) # -> 27
```

#### test_06:

```python
count_substring_at_most_k_distinct("racetracks", 2) # -> 19
```

#### test_07:

```python
count_substring_at_most_k_distinct("ab", 1) # -> 2
```

#### test_08:

```python
count_substring_at_most_k_distinct("ab", 2) # -> 3
```
