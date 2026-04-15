from math import inf
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        lookup = {}
        for i, v in enumerate(nums):
            if v not in lookup: lookup[v] = []
            lookup[v].append(i)
        
        best = inf
        for v in lookup.values():
            if len(v) < 3: continue
            best = min(best, 2 * min([v[i] - v[i-2] for i in range(2, len(v))]))
        return -1 if best == inf else best 