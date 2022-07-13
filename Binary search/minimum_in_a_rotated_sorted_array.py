def minimum_in_a_rotated_sorted_array(nums):
    l = 0
    r = len(nums) - 1 
    res = nums[0]
    
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        
        mid = (l+r) // 2
        res = min(res,nums[mid])
        
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
            
    return res

nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(minimum_in_a_rotated_sorted_array(nums))            