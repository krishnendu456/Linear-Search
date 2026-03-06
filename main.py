# Linear Search in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example list
numbers = [10, 25, 30, 45, 50, 65]

# Element to search
target = 45

# Call function
result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")