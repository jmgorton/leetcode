from typing import List
import functools
import operator

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # brute force
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            # nums[l:r+1:k] = (nums[l:r+1:k] * v) % MOD
            for i in range(l, r+1, k):
                nums[i] = nums[i] * v % MOD
        
        return functools.reduce(operator.xor, nums)
    
    ### TLE at 602/605