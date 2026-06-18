 # Linear Search

arr = [12, 25, 8, 45, 30, 18]

key = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element {key} found at position {i + 1}")
        found = True
        break

if not found:
    print(f"Element {key} not found in the array")