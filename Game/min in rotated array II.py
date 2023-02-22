def find_min_in_rotated_array(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        elif arr[mid] < arr[right]:
            right = mid

        elif arr[mid] == arr[right]:
            right = mid - 1
    return arr[left]


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7]
    print(find_min_in_rotated_array(arr))
