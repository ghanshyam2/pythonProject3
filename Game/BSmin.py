def binary_search_min(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        elif arr[mid - 1] > arr[mid]:
            return arr[mid]
        elif arr[mid] > arr[0]:
            left = mid + 1
        else:
            right = mid - 1


print(binary_search_min([3, 4, 5, 1, 2]))
print(binary_search_min([6, 7, 8,3, 4, 5]))
