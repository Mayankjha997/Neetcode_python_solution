def merge_interval(intervals):
    if intervals == []:
        return []
    res = [] 
    intervals.sort()
    for interval in intervals:
        if res == [] or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res

        