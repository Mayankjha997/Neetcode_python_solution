def contains_duplicate(nums):
    nums.sort()
    dic ={}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num] = 1
            
nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(contains_duplicate(nums))