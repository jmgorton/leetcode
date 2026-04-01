from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        ts = sum(sum(row) for row in grid)
        if ts % 2: return False

        hs = 0
        for row in grid:
            hs += sum(row) 
            if hs == ts // 2: return True
            elif hs > ts // 2: break
        
        vs = 0
        for col in zip(*grid):
            vs += sum(col) 
            if vs == ts // 2: return True
            elif vs > ts // 2: break

        return False