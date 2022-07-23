def pow(n,power):
    if power == 0:
        return 1
    if power < 0:
        return pow(1/n,-power)
    if power % 2 == 0:
        temp = pow(n,power/2)
        return temp * temp
    else:
        return n * pow(n,power - 1)
    
    
n = int(input("enter the number "))
power = int(input("enter the power "))
print(pow(n, power))