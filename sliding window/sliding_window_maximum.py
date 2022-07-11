import collections

def sliding_window_maximum(nums,k):
    l = 0
    r = 0
    q = collections.deque()
    output = []
    
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
        
        if r+1 >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output


nums = list(map(int,input("enter the numbers ").strip().split()))
k = int(input("enter the window size "))
print(nums)
print(sliding_window_maximum(nums,k))