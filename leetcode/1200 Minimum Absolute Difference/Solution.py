from typing import List
from itertools import pairwise
import math

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbsDist = math.inf
        ans = []
        for x in pairwise(arr): # print(x)
            if x[1] - x[0] < minAbsDist: 
                minAbsDist = x[1] - x[0]
                ans.clear()
            if x[1] - x[0] == minAbsDist:
                ans.append(list(x))
        # minAbsDist = min(map(lambda x: x[1] - x[0], pairwise(arr)))
        return ans

tests = [
    {
        "in": [4,2,1,3],
        "out": [[1,2],[2,3],[3,4]],
    },
    {
        "in": [1,3,6,10,15],
        "out": [[1,3]],
    },
    {
        "in": [3,8,-10,23,19,-4,-14,27],
        "out": [[-14,-10],[19,23],[23,27]],
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        if (act := sol.minimumAbsDifference(test["in"])) != test["out"]:
            print(f"Expected {test["out"]}; Actual {act}")