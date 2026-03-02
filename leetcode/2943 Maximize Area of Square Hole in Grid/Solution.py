from typing import List
# from itertools import pairwise

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # seems like all we have to do is count the longest streak of 
        # incrementing values in hBars and vBars and return the square 
        # of the minimum between the two

        if (not hBars or len(hBars) == 0 or not vBars or len(vBars) == 0): return 1
        vBars.sort()
        hBars.sort()
        hBarStreak = hBarBest = 1
        for i in range(1, len(hBars)):
            if (hBars[i] == hBars[i - 1] + 1): hBarStreak += 1
            else: hBarStreak = 1
            hBarBest = max(hBarBest, hBarStreak)
        vBarStreak = vBarBest = 1
        for i in range(1, len(vBars)):
            if (vBars[i] == vBars[i - 1] + 1): vBarStreak += 1
            else: vBarStreak = 1
            vBarBest = max(vBarBest, vBarStreak)
        return (min(vBarBest, hBarBest) + 1) ** 2
