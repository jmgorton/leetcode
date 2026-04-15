from typing import List
from math import inf

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        best = inf
        for i, v in enumerate(nums):
            if v != target: continue
            if abs(i - start) < best: best = abs(i - start)
            else: return best
        return best 