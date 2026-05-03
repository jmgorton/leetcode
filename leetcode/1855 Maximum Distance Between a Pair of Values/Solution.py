from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = best = 0 
        while i < len(nums1):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                best = max(best, j - i)
                j += 1
            i += 1
            j = max(j, i)
        return best