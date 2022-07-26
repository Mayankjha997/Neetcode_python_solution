def jump_game(jump):
    maxreach = 0
    for i in range(len(jump)):
        if i > maxreach:
            return False
        maxreach = max(maxreach, jump[i]+i)
    return True


jump = list(map(int,input("enter the numbers ").strip().split()))
print(jump)
print(jump_game(jump))