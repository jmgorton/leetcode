from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            temp = grid[x + i][y:y+k]
            grid[x + i] = grid[x + i][:y] + grid[x + k - i - 1][y:y+k] + grid[x + i][y+k:]
            grid[x + k - i - 1] = grid[x + k - i - 1][:y] + temp + grid[x + k - i - 1][y+k:]
        return grid