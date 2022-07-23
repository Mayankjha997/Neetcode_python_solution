def car_fleet(target,position,speed):
    pair = [(p,s) for p,s in zip(speed,position)]
    stack = []
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


target = int(input("enter the target "))
position = list(map(int,input("enter the cars position ").strip().split()))
speed = list(map(int,input("enter the cars position ").strip().split()))
print(position)
print(speed)
print(car_fleet(target,position,speed))