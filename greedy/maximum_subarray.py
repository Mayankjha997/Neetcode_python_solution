def maximum_subarray(nums):
    max_sum = total_sum = nums[0]
    for i in nums[1:]:
        total_sum = max(total_sum+i,i)
        max_sum = max(max_sum,total_sum)
        
    return max_sum


nums= list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(maximum_subarray(nums))