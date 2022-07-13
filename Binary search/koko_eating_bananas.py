import math
def koko_eating_bananas(piles,h):
    l = 1
    r = max(piles)
    res = r
    
    while l <= r:
        k = (l+r) // 2
        hour = 0
        for p in piles:
            hour+= math.ceil(p/k)
            
        if hour <= h:
            res = min(res,k)
            r = k - 1
        else:
            l = k + 1
        
    return res

piles = list(map(int,input("enter the piles ").strip().split()))
h = int(input("enter the threshold"))
print(piles)
print(koko_eating_bananas(piles,h))