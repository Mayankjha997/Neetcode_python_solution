def trapping_rain_water(height):
    res = 0
    left_max = 0
    right_max = 0
    l = 0
    r = len(height) - 1
    while l < r:
        left_max = max(left_max, height[l])
        right_max = max(right_max, height[r])
        if height[l] <= height[r]:
            res += left_max - height[l]
            l = l + 1
        else:
            res += right_max - height[r]
            r = r - 1
    return res
            
height = list(map(int,input("enter the numbers ").strip().split()))
print(height)
print(trapping_rain_water(height))