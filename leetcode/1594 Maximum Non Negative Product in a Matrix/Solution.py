from math import inf
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # pre = [[(1, 1)] * (len(grid[0]) + 1) for _ in (len(grid) + 1)]
        # pre = [(grid[0][0], grid[0][0])]
        pre = []
        for i, row in enumerate(grid):
            pre.append([])
            for j, el in enumerate(row):
                # best = [grid[i][j], grid[i][j]]
                # if i: best = (max(best[0], *(grid[i][j])))
                # best = [inf, -inf]
                # if i: best = (min([x * grid[i][j] for x in pre[i - 1][j]]), max([x * grid[i][j] for x in pre[i - 1][j]]))
                best = [grid[0][0], grid[0][0]]
                if i > 0:
                    best[0] = min(*(x * grid[i][j] for x in pre[i - 1][j]))
                    best[1] = max(*(x * grid[i][j] for x in pre[i - 1][j]))
                # if j: best = (min(best[0], *[x * grid[i][j] for x in pre[i][j - 1]]), max(best[1], *[x * grid[i][j] for x in pre[i][j - 1]]))
                if j > 0:
                    best[0] = min(best[0] if i > 0 else inf, *(x * grid[i][j] for x in pre[i][j - 1]))
                    best[1] = max(best[1] if i > 0 else -inf, *(x * grid[i][j] for x in pre[i][j - 1]))
                pre[-1].append(best[:])
        # print(pre)
        # return max(-1, int(max(pre[-1][-1]) % (10e9 + 7))) 
        if max(pre[-1][-1]) > -1: return max(pre[-1][-1]) % ((10 ** 9) + 7)
        return -1

