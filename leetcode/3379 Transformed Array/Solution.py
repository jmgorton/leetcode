from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        mod = len(nums)
        result = [0] * mod
        for i, v in enumerate(nums):
            result[i] = nums[(i + v) % mod]
        return result