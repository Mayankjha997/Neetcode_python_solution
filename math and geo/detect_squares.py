from collections import defaultdict
from ctypes import POINTER, pointer


class DetectSquares(object):

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []       
                

    def add(self, point):
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        
        

    def count(self, point):
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
    
    
obj = DetectSquares()
obj.add(pointer)
param_2 = obj.count(POINTER)