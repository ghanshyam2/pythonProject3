def nineDivisors(N):
    divisor = 1
    # count = 0
    counts = 0

    while divisor <= N:
        divid = 1
        count = 0
        while divid <= divisor:
            if divisor % divid == 0:
                count += 1
            divid += 1
        divisor += 1
        if count == 9:
            counts += 1
    return counts


print(nineDivisors(50))
print(nineDivisors(100))
print(nineDivisors(1000))
