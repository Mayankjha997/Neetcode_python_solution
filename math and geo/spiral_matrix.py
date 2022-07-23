from numpy import mat


def spiral_matrix(matrix):
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)
    col_end = len(matrix[0])
    res = []
    while row_begin < row_end and col_begin < col_end:
        for i in range(col_begin,col_end):
            res.append(matrix[row_begin][i])
            
        for j in range(row_begin+1,row_end-1):
            res.append(matrix[j][col_end-1])
            
        if row_end != row_begin+1 :
            for x in range(col_end-1,col_begin-1,-1):
                res.append(matrix[row_end-1][x])
                
        if col_end != col_begin+1:
            for z in range(row_end-2,row_begin,-1):
                res.append(matrix[z][col_begin])
                
        row_begin += 1
        col_begin += 1
        row_end -= 1
        col_end -= 1
                
    return res


matrix = []
rows = int(input("enter the rows "))
cols = int(input("enter the columns "))
for r in range(rows):
    v = []
    for c in range(cols):
        z = int(input("enter the number "))
        v.append(z)
    matrix.append(v)

print(matrix)
print(spiral_matrix(matrix))
            