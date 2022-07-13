def search_a_2d_matrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    top = 0
    bot  = rows - 1
    
    while top <= bot:
        mid = (top+bot) // 2
        if target < matrix[mid][0]:
            bot = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break
        
    if not top <= bot:
        return False
    
    mid = (top + bot)//2
    l = 0
    r = cols - 1
    while l<=r:
        m = (l+r)//2
        if target < matrix[mid][m]:
            l = m + 1
        elif target > matrix[mid][m]:
            r = r - 1
        else:
            return True
    
    return False


matrix = []
target = int(input("enter the target value"))
rows = int(input("enter the rows "))
cols = int(input("enter the columns "))
for i in range(rows):
    v = []
    for j in range(cols):
        z = int(input("enter the number"))
        v.append(z)
    matrix.append(v)
print(matrix)
print(search_a_2d_matrix(matrix,target))
 
            