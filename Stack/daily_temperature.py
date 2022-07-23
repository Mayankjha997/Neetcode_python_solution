def daily_temperature(temperature):
    res = [0] * len(temperature)
    stack = []
    
    for i,t in enumerate(temperature):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            res[stackI] = (i - stackI)
        
        stack.append([t,i])
        
    return res

temperature = list(map(int,input("enter the temperature ").strip().split()))
print(temperature)
print(daily_temperature(temperature))    
    
    
    
    