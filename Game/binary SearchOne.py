def binary_search(arr, k):
    # arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 4, 6, 9, 10, 5, 7]
    k = 5
    print(binary_search(arr, k))
