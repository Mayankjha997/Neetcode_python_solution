def valid_palindrome(s):
    res = " "
    for i in s:
        if i.isalnum():
            res+=i.lower()
            
    l = 0
    r = len(res) - 1
    if res[l] != res[r]:
        return False
    else:
        l = l + 1
        r = r - 1
        return True
    
    
s = input("enter the string")
print(s)
print(valid_palindrome(s))
            