from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        best = 0 
        for i in range(-1, -len(colors), -1):
            if colors[i] == colors[0]: continue
            best = len(colors) + i
            break
        for i in range(len(colors)):
            if colors[i] == colors[-1]: continue
            best = max(best, len(colors) - i - 1)
            break
        return best 