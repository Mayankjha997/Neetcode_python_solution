def set_matrix_to_zero(matrix):
    rows= len(matrix)
    cols = len(matrix[0])
    row_zero = False
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True  
 
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
                
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
        
    if row_zero == True:
        for c in range(cols):
            matrix[0][c] = 0
            
    return matrix
                 
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
print(set_matrix_to_zero(matrix))
                
        