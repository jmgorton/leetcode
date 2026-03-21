from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        pre = [[0] * len(grid[0]) for _ in range(len(grid))]
        result = 0
        for j, row in enumerate(grid):
            # pre.append([])
            for i, el in enumerate(row):
                sm = (pre[j][i - 1] if (i > 0) else 0) + (pre[j - 1][i] if (j > 0) else 0) - (pre[j - 1][i - 1] if (j and i) else 0) + el
                # pre[-1].append(sm) 
                pre[j][i] = sm
                if sm <= k: result += 1
        # print(pre)
        return result 