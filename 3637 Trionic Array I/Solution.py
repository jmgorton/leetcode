from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        hasPeak = hasTrough = False
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                if hasPeak or hasTrough: return False # peak must come first, no more and no less than one peak
                hasPeak = True
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                if hasTrough: return False # exactly one trough in full array 
                hasTrough = True
        return hasPeak and hasTrough