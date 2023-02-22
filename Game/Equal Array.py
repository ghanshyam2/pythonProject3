def equal_array(arr, ar):
    arr.sort()
    ar.sort()
    # ar.sort()
    m = len(arr) - 1
    n = len(ar) - 1
    count = 0
    i = j = 0

    while i <= m and j <= n:

        if arr[i] == ar[j]:
            count += 1
        i += 1
        j += 1
    return count == len(arr)


print(equal_array([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))
print(equal_array([2, 5, 6], [2, 5, 17]))
print(equal_array([2, 0, 0, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]))
