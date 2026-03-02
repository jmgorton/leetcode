from typing import List
import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = math.inf
        j = k - 1
        nums.sort()
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[j] - nums[i])
            j += 1
        return ans