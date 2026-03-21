from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # pre = [[0] for _ in range(len(grid) + 1)]
        # pre[0] = [0] * (len(grid[0]) + 1)
        pre = [([(0, False)] * (len(grid[0]) + 1)) for _ in range(len(grid) + 1)]
        result = 0
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                hasX = pre[i + 1][j][1] or pre[i][j + 1][1] or el == 'X'
                pre[i + 1][j + 1] = (pre[i][j + 1][0] + pre[i + 1][j][0] - pre[i][j][0] + (1 if el == 'X' else (-1 if el == 'Y' else 0)), hasX)
                # pre[i + 1][j + 1] -= pre[i][j]
                # if el == 'X': pre[i + 1][j + 1] += 1
                # elif el == 'Y': pre[i + 1][j + 1] -= 1 
                if pre[i + 1][j + 1][0] == 0 and pre[i + 1][j + 1][1]: result += 1
        return result 