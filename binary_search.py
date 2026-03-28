def binary_search(arr, key, low, high): 

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)



n = int(input("Enter number of elements: "))

arr = []
print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

result = binary_search(arr, key, 0, n-1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")