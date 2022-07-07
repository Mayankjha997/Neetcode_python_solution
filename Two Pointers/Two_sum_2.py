def two_sum(numbers, target):
    r = len(numbers) - 1
    l = 0
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1 , r+1]
        elif numbers[l] + numbers[r] > target:
            r = r - 1
        else:
            l = l + 1


numbers = list(map(int,input("enter the numbers ").strip().split()))
target = int(input("enter the target ")) 
print(numbers)
print(two_sum(numbers , target))