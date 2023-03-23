def buy_stock_sell(arr):
    left, right = 0, 1
    max_profit = 0

    while right < len(arr) - 1:

        if arr[left] < arr[right]:
            profit = arr[right] - arr[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit


print(buy_stock_sell([7, 1, 5, 3, 6, 4]))
#print(buy_stock_sell([7, 6, 4, 3, 1]))

#print(int('puppy'))
