def search_in_a_rotated_sorted_array(nums,target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l] :
                l = mid + 1
            else:
                r = mid -1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

nums = list(map(int,input("enter the numbers ").strip().split()))
target = int(input("enter the target "))
print(nums)
print(search_in_a_rotated_sorted_array(nums,target))
             

            
             