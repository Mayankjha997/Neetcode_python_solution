def best_time_to_buy_and_sell_stock(stocks):
    if not stocks:
        return 0
    ans = 0
    mini = stocks[0]
    for i in range(1,len(stocks)):
        if stocks[i] < mini:
            mini = stocks[i]
        else:
            ans = max(ans, stocks[i] - mini)
    return ans

nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(best_time_to_buy_and_sell_stock(nums))