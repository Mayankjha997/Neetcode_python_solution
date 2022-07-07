def container_with_most_water(height):
    res= 0 
    l = 0
    r = len(height) - 1
    while l < r:
        res = max(res , (r-l)*min(height[l],height[r]))
        if height[l] < height[r]:
            l = l + 1
        else:
            r = r - 1
    return res

height = list(map(int,input("enter the numbers ").strip().split()))
print(height)
print(container_with_most_water(height))