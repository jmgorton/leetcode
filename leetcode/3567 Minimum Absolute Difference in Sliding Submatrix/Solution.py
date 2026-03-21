from typing import List
from itertools import pairwise

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = [] 
        m, n = len(grid), len(grid[0]) 
        for i in range(m - k + 1):
            ans.append([])
            for j in range(n - k + 1):
                flat = {x for ik in range(i, i+k) for x in grid[ik][j:j+k]}
                ans[-1].append(min((x[1] - x[0] for x in pairwise(sorted(flat)))) if len(flat) > 1 else 0)
        return ans