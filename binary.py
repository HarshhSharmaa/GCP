def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# User Input
arr = list(map(int, input("Enter sorted elements separated by space: ").split()))

target = int(input("Enter element to search: "))

# Function Call
result = binary_search(arr, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
