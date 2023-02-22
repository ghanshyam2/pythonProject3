def binary_search(arr, k):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1


def find_all_occurrence(arr, k):
    index = binary_search(arr, k)
    ind = [index]
    ind_x = index - 1
    while ind_x >= 0:
        if arr[ind_x] == k:
            ind.append(ind_x)
        else:
            break
        ind_x -= 1
    indxx = index + 1
    while indxx < len(arr):
        if arr[indxx] == k:
            ind.append(indxx)
        else:
            break
        indxx += 1
    return sorted(ind)


if __name__ == "__main__":
    arr= [1,4,6,9,11,15,15,15,17,21,34,34,56]
    # arr = [1, 2, 3, 4, 5, 5, 5, 13, 18, 99]
    k = 15
    # k = 5
    print(find_all_occurrence(arr, k))
