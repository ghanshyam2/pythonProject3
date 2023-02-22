from bisect import bisect_left

''' bisect : finds and returns the position at which an element can be inserted into a Python list 
         while maintaining the sorted order of the Python list.'''


def count_smaller_than_self(arr):
    res = []
    sortArr = []

    for num in arr[::-1]:
        index = bisect_left(sortArr, num)
        res.append(index)
        sortArr.insert(index, num)

    return res[::-1]


print(count_smaller_than_self([5, 2, 6, 1, 3]))
