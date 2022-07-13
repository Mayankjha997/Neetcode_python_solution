def longes_consecutive_sequences(nums):
    numset = set(nums)
    
    longest = 0
    for n in nums:
        if (n-1) not in numset:
            length = 0
            while length+n in numset:
                length+=1
            longest = max(length,longest)
    return longest

nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
print(longes_consecutive_sequences(nums))
                