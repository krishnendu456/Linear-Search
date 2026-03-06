# Linear Search in Python

This repository contains a simple implementation of the **Linear Search algorithm** using Python.

##  What is Linear Search?

Linear Search is one of the simplest searching algorithms. It checks each element in a list sequentially until the desired element is found or the list ends.

##  Algorithm Steps

1. Start from the first element of the list.
2. Compare each element with the target value.
3. If the element matches the target, return its index.
4. If the element is not found after checking all elements, return **-1**.

##  Python Code

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 25, 30, 45, 50, 65]
target = 45

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
```

##  Example Output

```
Element found at index: 3
```

##  How to Run

1. Clone the repository
2. Run the Python file

```
python linear_search.py
```

##  Concepts Used

* Python Functions
* Lists
* Loops
* Basic Searching Algorithms

