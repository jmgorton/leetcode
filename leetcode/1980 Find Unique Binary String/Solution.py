from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ''
        for i, v in enumerate(nums):
            result += '1' if v[i] == '0' else '0'
        return result