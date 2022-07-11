def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
nums = list(map(int,input("enter the numbers ").strip().split()))
target = int(input("enter the target number "))
print(nums)
print(two_sum(nums, target))