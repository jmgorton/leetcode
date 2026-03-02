from typing import List
from heapq import heapify, heappushpop

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        # heap = nums[1:3]
        # if heap[0] > heap[1]: heap[0], heap[1] = heap[1], heap[0]
        heap = sorted([-x for x in nums[1:3]])
        # heap = heapify(nums[1:3])
        for val in nums[3:]:
            heappushpop(heap, -val)
        return cost - sum(heap) 