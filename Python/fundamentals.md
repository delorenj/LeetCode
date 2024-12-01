# Python Data Structures Quick Reference

## Table of Contents
- [Array Creation](#array-creation)
- [Arrays/Lists](#arrayslists)
- [Strings](#strings)
- [Ranges](#ranges)
- [Reverse](#reverse)
- [Debug Printing](#debug-printing)
- [Dictionaries](#dictionaries)
- [Sets](#sets)

## Array Creation
```python
# Basic initialization
arr = []                           # Empty list
arr = [1, 2, 3]                    # With values
arr = list()                       # Empty list constructor

# Fixed-size arrays
arr = [0] * n                      # n zeros
arr = [False] * n                  # n boolean values
arr = [[0] * cols for _ in range(rows)]  # 2D array

# List comprehension
arr = [i for i in range(n)]        # 0 to n-1
arr = [i * 2 for i in range(n)]    # Even numbers
arr = [x for x in arr if x > 0]    # Filter positive

# From other types
arr = list("abc")                  # From string: ['a','b','c']
arr = list(range(5))               # From range: [0,1,2,3,4]
```

## Arrays/Lists
```python
arr = [1, 2, 3]

# Index and value
for i in range(len(arr)):           # [0,1,2]
for x in arr:                       # 1,2,3
for i, x in enumerate(arr):         # (0,1), (1,2), (2,3)

# Slicing
for x in arr[start:end:step]:       # Flexible slicing
```

## Strings
```python
s = "abc"

for c in s:                         # Character iteration
for i, c in enumerate(s):           # Index and character
```

## Ranges
```python
for i in range(n):                  # 0 to n-1
for i in range(start, end):         # start to end-1
for i in range(start, end, step):   # With custom step
```

## Reverse
```python
for x in reversed(arr):             # Reverse iteration
for i in range(len(arr)-1, -1, -1): # Reverse with index
```

## Debug Printing
```python
print(x)                            # Basic print
print(f"Value: {x}")               # f-string formatting
print("Val:", x, "Index:", i)      # Multiple values
print(arr)                         # Print full list
print(*arr)                        # Unpack list items
```

## Dictionaries
```python
# Creation
d = {}                             # Empty dict
d = {"a": 1, "b": 2}              # With key-values
d = dict(a=1, b=2)                # Using dict()
d = {x: 0 for x in range(5)}      # Dict comprehension

# Operations
d[key] = value                     # Set/update
value = d[key]                     # Get (raises KeyError)
value = d.get(key, default)        # Get with default
key in d                           # Check existence
d.pop(key)                         # Remove and return
d.update(other_dict)               # Merge dicts

# Iteration
for key in d:                      # Keys
for key, value in d.items():       # Key-value pairs
for value in d.values():           # Values

# Get values from keys
values = [d[k] for k in keys]      # List comprehension
values = list(map(d.get, keys))    # Using map
values = list(d.values())          # All values
```

## Sets
```python
# Creation
s = set()                          # Empty set
s = {1, 2, 3}                      # With values
s = set([1, 2, 3])                # From list

# Operations
s.add(x)                           # Add element
s.remove(x)                        # Remove (raises KeyError)
s.discard(x)                       # Remove (no error)
x in s                             # Check existence

# Set operations
s1 | s2                           # Union
s1 & s2                           # Intersection
s1 - s2                           # Difference
s1 ^ s2                           # Symmetric difference
