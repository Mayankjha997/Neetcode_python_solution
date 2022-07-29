def surrounded_regions(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "O" and (i in [0,rows-1] or j in [0,cols-1]):
                capture(grid,i,j)
                
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "O":
                grid[i][j] = "X"
                
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "T":
                grid[i][j] = "O"


def capture(grid,i,j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "O":
        return 
    
    grid[i][j] = "T"
    capture(grid,i+1,j) 
    capture(grid,i-1,j)
    capture(grid,i,j+1) 
    capture(grid,i,j-1)          