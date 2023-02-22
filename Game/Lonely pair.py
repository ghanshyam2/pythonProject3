def lonely(arr):
    frq, list_ = {},[]

    for s in arr:
        if s not in frq:
            frq[s] = 1
        else:
            frq[s] += 1
    for n in frq:
        if frq[n] == 1 and (n-1) not in frq and (n+1) not in frq:
            list_.append(n)
    return list_


print(lonely([10, 6, 5, 8]))
print(lonely([1,3,5,3]))
print(lonely([2,4,6,8,9,10]))
