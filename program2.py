# Binary Search

arr = [5, 10, 15, 20, 25, 30, 35, 40]  # Sorted array
key = int(input("Enter the element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print(f"Element {key} found at position {mid + 1}")
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Element {key} not found in the array")