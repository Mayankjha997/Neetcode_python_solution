def happy_number(num):
    visit = set()
    while num not in visit:
        visit.add(num)
        num = square(num)
        if num == 1:
            return True
    return False


def square(num):
    output = 0
    while num:
        digit = num%10
        digit = digit ** 2
        output+=digit
        num = num // 10
        
    return output

num = int(input("enter the number "))
print(happy_number(num))