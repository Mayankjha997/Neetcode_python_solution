from heapq import heappush, heappushpop


def top_k_frequent_element(nums , k):
    dic = {}
    ans = []
    
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    
    for key, value in dic.items():
        if len(ans) < k:
            heappush(ans,[value,key])
        else:
            heappushpop(ans,[value,key])
            
    return [key for value,key in ans]

nums = list(map(int,input("enter the numbers ").strip().split()))
k = int(input("enter the frequent element "))
print(nums)
print(top_k_frequent_element(nums,k))