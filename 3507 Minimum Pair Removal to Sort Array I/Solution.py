from typing import List 
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # i = ans = 0
        # si = nums[i]
        # while i < len(nums):
        #     j = i + 1
        #     # if j == len(nums): return ans
        #     sj = 0
        #     while j < len(nums) and sj < si:
        #         sj += nums[j]
        #         j += 1
        #     if j < len(nums): ans += j - i - 2
        #     else: 
        #         if sj < si: ans += 1
        #         return ans 
        #     # ans += j - i - 1
        #     si = sj
        #     i = j - 1

        # ***** FAIL *****

        heap = []
        next = {x: x+1 for x in range(len(nums))}
        next[len(nums)-1] = None
        decr = set()
        for i, v in enumerate(nums[:-1]):
            heapq.heappush(heap, (v + nums[i+1], i, next[i]))
            if nums[i+1] < v: decr.add(i)
        ans = 0
        while decr and heap:
            (nv, nvi, pnvi) = heapq.heappop(heap)
            if not next[pnvi]: continue
            ans += 1
            nums[nvi] = nv
            next[nvi] = next[pnvi]
            if next[pnvi]:
                if nums[next[pnvi]] >= nums[nvi] and nvi in decr: decr.remove(nvi)
                heapq.heappush(heap, (nums[next[nvi]] + nums[nvi], nvi, next[nvi]))
            next[pnvi] = None
        return ans


testCases = [
    {
        "in": [5,2,3,1],
        "out": 2
    },
    {
        "in": [1,2,2],
        "out": 0
    },
    {
        "in": [5],
        "out": 0
    },
    {
        "in": [2,2,-1,3,-2,2,1,1,1,0,-1],
        # [2,2,-1,3,0,1,1,1,0,-1] 1
        # [2,2,-1,3,0,1,1,1,-1] 2
        # [2,2,-1,3,0,1,1,0] 3
        # [2,1,3,0,1,1,0] 4 ... ah, shoot, i was wrong 
        # [2,1,3,1,1,0] 5
        # [2,1,3,1,1] 6
        # [2,1,3,2] 7
        # [3,3,2] 8
        # [3,5] 9
        "out": 9
    },
    {
        "in": [-2,1,2,-1,-1,-2,-2,-1,-1,1,1],
        # [-2,1,2,-1,-1,-4,None,-1,-1,1,1] 1
        "out": 10
    }
]
            
if __name__ == "__main__":
    sol = Solution()
    for test in testCases:
        if (act := sol.minimumPairRemoval(test["in"])) != test["out"]:
            print(f"Expected {test['out']}; Got {act}")
        else: print("Success")