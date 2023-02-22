def binary_search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[left] <= target < arr[mid]:
            right = mid - 1
        elif arr[mid] < target <= arr[right]:
            left = mid + 1
        elif arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search_rotated([4, 5, 6, 1, 2, 3], 0))
print(binary_search_rotated([4, 5, 6, 1, 2, 3], 2))
print(binary_search_rotated([4, 5, 6, 1, 2, 3], 4))
