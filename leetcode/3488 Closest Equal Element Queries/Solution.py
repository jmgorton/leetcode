from typing import List
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        lookup = {}
        for i, v in enumerate(nums):
            if v not in lookup: lookup[v] = []
            lookup[v].append(i) 
        
        result = []
        for i in queries:
            if len(lookup[nums[i]]) == 1:
                result.append(-1)
                continue
            ix = bisect.bisect_left(lookup[nums[i]], i)
            bl = (lookup[nums[i]][ix] - lookup[nums[i]][ix - 1] + len(nums)) % len(nums) # inf
            # if ix > 0: bl = lookup[nums[i]][ix] - lookup[nums[i]][ix - 1]
            # else: bl = len(nums) - lookup[nums[i]][ix] + lookup[nums[i]][ix - 1]

            br = (lookup[nums[i]][(ix + 1) % len(lookup[nums[i]])] - lookup[nums[i]][ix] + len(nums)) % len(nums) # inf
            # if ix == len(lookup[nums[i]]) - 1:
            #     br = len(nums) - lookup[nums[i]][ix] + lookup[nums[i]][0]
            # else: br = lookup[nums[i]][ix + 1] - lookup[nums[i]][ix]
            result.append(min(bl, br))
        return result 