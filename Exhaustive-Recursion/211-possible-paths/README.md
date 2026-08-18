## possible paths

Write a function that takes in a graph adjacency list, a source node, and a destination node. The
function should return a list containing all possible paths that travel between the source and
destination.

You can assume that the graph is a DAG (directed-acyclic-graph).

#### test_00:

```python
graph = {
  "a": ["b", "c", "d"],
  "b": ["d"],
  "c": ["d"],
  "d": []
}
possible_paths(graph, "a", "d") # ->
# [
#   ["a", "b", "d"],
#   ["a", "c", "d"],
#   ["a", "d"]
# ]
```

#### test_01:

```python
graph = {
  "a": ["b", "c", "d"],
  "b": ["d"],
  "c": ["d"],
  "d": []
}
possible_paths(graph, "c", "b") # ->
# []
```

#### test_02:

```python
graph = {
  "a": ["b", "d"],
  "b": ["c", "e"],
  "c": ["e"],
  "d": ["b", "f"],
  "e": ["f"],
  "f": []
}
possible_paths(graph, "a", "c") # ->
# [
#   ["a", "b", "c"],
#   ["a", "d", "b", "c"]
# ]
```

#### test_03:

```python
graph = {
  "a": ["b", "d"],
  "b": ["c", "e"],
  "c": ["e"],
  "d": ["b", "f"],
  "e": ["f"],
  "f": []
}
possible_paths(graph, "a", "f") # ->
# [
#   ["a", "b", "c", "e", "f"],
#   ["a", "b", "e", "f"],
#   ["a", "d", "b", "c", "e", "f"],
#   ["a", "d", "b", "e", "f"],
#   ["a", "d", "f"]
# ]
```
