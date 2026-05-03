from typing import List
from math import inf

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        occ = {}
        rem = None
        for row in grid:
            for v in row:
                q, r = divmod(v, x)
                if rem is None: rem = r
                if rem != r: return -1 
                if q not in occ: occ[q] = 0
                occ[q] += 1
        
        pre = [0] * len(occ)
        prevV = None
        prevC = 0
        for i, v in enumerate(sorted(occ.keys())):
            if prevV is not None:
                pre[i] = pre[i - 1] + ((v - prevV) * prevC)
            prevV = v
            prevC += occ[v]
        
        post = [0] * len(occ) 
        prevV = None
        prevC = 0
        for i, v in enumerate(sorted(occ.keys(), reverse=True)):
            if prevV is not None:
                post[i] = post[i - 1] + ((prevV - v) * prevC)
            prevV = v
            prevC += occ[v]
        
        # print(pre)
        # print(post)

        best = inf
        for a, b in zip(pre, post[::-1]):
            # print(a, b)
            best = min(best, a + b)
        return best 