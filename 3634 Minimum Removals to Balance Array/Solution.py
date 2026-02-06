from typing import List
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # mins = []
        # maxes = []
        # for v in nums:
        #     heappush(mins, v)
        #     heappush(maxes, -v)
        
        nums.sort()
        i = 0 
        j = len(nums) - 1

        while nums[i] * k < nums[j]:
            # if j == i + 1: break
            ib = bisect_right(nums, nums[i] * k)
            if ib > j: break
            # print(f"-({nums[j]} // {-k}) == {-(nums[j] // -k)}")
            jb = bisect_left(nums, -(nums[j] // -k)) # TODO validate 
            # print(f"At j={j}: jb={jb}")
            if jb <= i: break
            if ib - i > j - jb: j -= 1
            else: i += 1

        
        return i + (len(nums) - j - 1)

tests = [
    {
        "in": ([2,1,5], 2),
        "out": 1
    },
    {
        "in": ([1,6,2,9], 3),
        "out": 2
    },
    {
        "in": ([4,6], 2),
        "out": 0
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        actual = sol.minRemoval(*test["in"])
        assert actual == test["out"], f"Expected {test["out"]}, got {actual}"
    print("All tests passed.")