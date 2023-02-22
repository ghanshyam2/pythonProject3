def insert_position(arr, k):
    left, right = 0, len(arr) - 1
    res = -1
    if k > arr[-1]:
        return len(arr)
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            return mid

        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
            res = mid
    return res


print(insert_position([1, 2, 3, 4], 3.5))
print(insert_position([2,3,1,6,5,8], 7))
