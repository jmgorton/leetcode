class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dist = 0
        for i in range(1, len(points)):
            dist += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return dist

from itertools import pairwise
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # zip(*points)
        return sum([max(abs(x[0] - y[0]), abs(x[1] - y[1])) for x, y in pairwise(points)])
