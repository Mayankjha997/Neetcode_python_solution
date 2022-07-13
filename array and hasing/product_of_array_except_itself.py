def product_of_array_except_itself(nums):
    left = [1] * len(nums)
    for i in range(1,len(nums)):
        left[i] = left[i-1] * nums[i-1]
    
    right = [1] * len(nums)
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
        
    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] = right[i] * left[i] 
        
    return res

nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(product_of_array_except_itself(nums))   