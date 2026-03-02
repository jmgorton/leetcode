# ******** LeetCode Editorial: *********

# Use Segment Tree to maintain dynamic horizontal coverage (critical x-coords and depths) 
# "As the scan line moves upward, each event updates a continuous x-interval, which is an 
#   interval update. Therefore, a segment tree with lazy propagation is required."
# Each node of the Segment Tree maintains
#   - the coverage count of the interval
#   - the total covered length of the interval (when coverage count > 0) 
# "In practice, we can avoid performing a second scan by recording the covered area and 
#   horizontal coverage for each height interval during the first scan, and then locating 
#   the correct interval using traversal or binary search."

from typing import List
from bisect import *
import SegmentTree

class OfficialSolution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xCoordsSet = set()
        for xi, yi, li in squares:
            events.append((yi, 1, xi, xi + li))
            events.append((yi + li, -1, xi, xi + li))
            xCoordsSet.update([xi, xi + li])
        xCoords = sorted(xCoordsSet)

        segTree = SegmentTree(xCoords)
        events.sort()

        pSum = []
        widths = []
        totalArea = 0
        prevY = events[0][0]

        # scan to calculate total area and record intermediate states 
        for y, delta, xl, xr in events:
            length = segTree.query()
            totalArea += length * (y - prevY)
            # qleft = xl; qright = xr; qval = delta; left = 0; right = segTree.n - 1; pos = 0
            segTree.update(xl, xr, delta, 0, segTree.n - 1, 0) 
            # record prefix sums and widths
            pSum.append(totalArea)
            widths.append(segTree.query())
            prevY = y
        
        # calculate target area rounded up
        target = (totalArea + 1) // 2
        # find the first position >= target using binary search (bisect) 
        i = bisect_left(pSum, target) - 1
        # get the corresponding area, width, and height
        area = pSum[i]
        width = widths[i]
        height = events[i][0]

        return height + (totalArea - area * 2) / (width * 2) 
