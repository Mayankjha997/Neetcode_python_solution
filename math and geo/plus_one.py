def plus_one(num):
    num = num[::-1]
    carry = 1
    i = 0
    while carry:
        if i < len(num):
            if num[i] == 9:
                num[i] = 0
            else:
                num[i] += 1
                carry = 0
        else:
            num.append(1)
            carry = 0
    
        i+= 1
    return num[::-1] 

num = list(map(int,input("enter the numbers ").strip().split()))
print(num)
print(plus_one(num))  