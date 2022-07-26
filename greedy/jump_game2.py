def jump_game2(jump):
    l = 0
    r = 0
    res = 0
    while r < len(jump) - 1:
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest,i+jump[i])
        
        l = r + 1
        r = farthest
        res+=1
    return res

jump = list(map(int,input("enter the numbers ").strip().split()))
print(jump)
print(jump_game2(jump))