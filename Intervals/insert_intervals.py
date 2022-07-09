from hashlib import new


def insert_intervals(intervals,new_intervals):
    i = 0
    res = []
    while i < len(intervals) and new_intervals[0] > intervals[i][0]:
        res.append(intervals[i])
        i+=1
    
    if res == [] or res[-1][1] < new_intervals[0]:
        res.append(new_intervals)
    else:
        res[-1][1] = max(res[-1][1] , new_intervals[1])
        
    while i < len(new_intervals):
        if res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1] , intervals[i][1])
        i+=1
    return res    



           