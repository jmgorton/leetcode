from typing import List
from itertools import accumulate

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1: return False
        # lookup = {val: (i, j) for i, row in enumerate(grid) for j, val in enumerate(row)}
        lookup = {}
        total = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val not in lookup: lookup[val] = []
                lookup[val].append((i, j)) 
                total += val
        # row_sums = [sum(row) for row in grid]
        # pre_rows = [0]
        # for rs in row_sums:
        #     pre_rows.append(pre_row[-1] + rs)
        pre_rows = accumulate([sum(row) for row in grid])
        # pre_row.popleft()
        for i, prs in enumerate(pre_rows):
            diff = total - prs - prs
            if diff == 0: return True
            # if i < 1 or m - i < 2: continue

            if diff in lookup:
                if i < 1 or m - i < 2:
                    if any(x[0] >= i and (x[1] == 0 or x[1] == m - 1) for x in lookup[diff]):
                        return True
                else:
                    if any(x[0] >= i for x in lookup[diff]): 
                        return True
            if -diff in lookup:
                if i < 1 or m - i < 2:
                    if any(x[0] < i and (x[1] == 0 or x[1] == m - 1) for x in lookup[-diff]):
                        return True
                else:
                    if any(x[0] < i for x in lookup[-diff]): 
                        return True
        # col_sums = [sum(col) for col in zip(*grid)]
        pre_col = accumulate([sum(col) for col in zip(*grid)])
        for i, pcs in enumerate(pre_col):
            diff = total - pcs - pcs
            if diff == 0: return True
            # if i < 1 or n - i < 2: continue
            # if diff in lookup and any(x[1] >= i for x in lookup[diff]): return True
            if diff in lookup:
                if i < 1 or n - i < 2: 
                    if any(x[1] >= i and (x[0] == 0 or x[0] == n - 1) for x in lookup[diff]): 
                        return True
                else:
                    if any(x[1] >= i for x in lookup[diff]):
                        return True
            if -diff in lookup:
                if i < 1 or n - i < 2:
                    if any(x[1] < i and (x[0] == 0 or x[0] == n - 1) for x in lookup[diff]):
                        return True
                else:
                    if any(x[1] < i for x in lookup[-diff]): 
                        return True
        
        return False