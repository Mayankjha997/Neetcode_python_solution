def rotten_oranges(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    rotten = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2]
    count  = 0
    while rotten:
        rotten = rotting(grid,rotten)
        if len(rotten) == 0:
            break
        count+=1
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1
    
    return count


def rotting(grid,rotten):
    temp = []
    for i,j in rotten:
        if i > 0 and grid[i-1][j] == 1:
            temp.add((i-1,j))
            grid[i-1][j] = 2
            
        if i < len(grid) - 1 and grid[i+1][j] == 1:
            temp.add((i+1,j))
            grid[i+1][j] = 2
            
        if j > 0 and grid[i][j+1] == 1:
            temp.add((i,j+1))
            grid[i+1][j] = 2
            
        if j < len(grid[0]) - 1 and grid[i][j-1] == 1:
            temp.add((i,j-1))
            grid[i+1][j] = 2
            
    return temp