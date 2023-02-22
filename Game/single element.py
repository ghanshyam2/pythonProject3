def single_element(arr):
    count = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
    return arr[count]


print(single_element([1, 1, 2, 2, 3, 4, 4, 5, 5]))
print(single_element([3,3,7,7,10,11,11]))
