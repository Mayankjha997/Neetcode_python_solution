def gas_station(gas,cost):
    start = 0
    tank = 0
    shortage = 0
    for i in range(len(gas)):
        tank += gas[i]
        if tank >= cost[i]:
            tank -= cost[i]
        else:
            shortage += cost[i] - tank
            start = i + 1
            tank = 0
        
    if start == len(gas) or tank < shortage:
        return -1
    
    return start


gas = list(map(int,input("enter the gas").strip().split()))
cost = list(map(int,input("enter the gas").strip().split()))
print(gas)
print(cost)
print(gas_station(gas,cost))
