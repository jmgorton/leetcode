from typing import List

class SegmentTree:
    def __init__(self, xCoords: List[int]):
        self.xCoords = xCoords
        self.n = len(xCoords) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    
    # this is where most of the magic happens... 
    # 
    def update(self, qleft, qright, qval, left, right, pos):
        if self.xCoords[right + 1] <= qleft or self.xCoords[left] >= qright:
            return
        if qleft <= self.xCoords[left] and self.xCoords[right + 1] <= qright:
            self.count[pos] += qval
        else:
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)
        
        if self.count[pos] > 0:
            self.covered[pos] = self.xCoords[right + 1] - self.xCoords[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = (self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2])
    
    # this just returns the covered area across a horizontal slice (pos y) as the scan progresses
    def query(self):
        return self.covered[0]