def course_schedule(numcourses,prerequisites):
    premap = {i : [] for i in range(numcourses)}
    for crs,pre in premap:
        premap[crs].append(pre)
    visited = set()
    for crs in range(numcourses):
        if not dfs(crs):
            return False
    
def dfs(crs,visited,premap):
    if crs in visited:
        return False
    
    if premap[crs] == []:
        return True
    
    visited.add(crs)
    
    for pre in premap[crs]:
        if not dfs(pre):
            return False
        
    visited.remove(crs)
    premap[crs] = []
    return True
     