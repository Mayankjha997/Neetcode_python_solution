def non_overlapping_intervals(intervals):
    close = float("-inf")
    for interval in sorted(intervals, key = lambda s : s[1]):
        if interval[0] >= close:
            close = interval[1]
        else:
            count+=1
    return count 