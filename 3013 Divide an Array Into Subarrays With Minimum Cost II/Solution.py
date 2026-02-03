from typing import List
from heapq import heapify, heappop, heappush # heappushpop

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ### PREV SOLUTION
        ### (was k=3, and no dist criteria between second and last indices)
        # def minimumCost(self, nums: List[int]) -> int:
        #     cost = nums[0]
        #     # heap = nums[1:3]
        #     # if heap[0] > heap[1]: heap[0], heap[1] = heap[1], heap[0]
        #     heap = sorted([-x for x in nums[1:3]])
        #     # heap = heapify(nums[1:3])
        #     for val in nums[3:]:
        #         heappushpop(heap, -val)
        #     return cost - sum(heap) 

        ### NEW SOLUTION
        # this problem can start off similarly, with a heap of minimum 
        # indices to get the ideal placement irrespective of the dist 
        # but we keep all elements in the heap with their vals and indices
        # then we look at the first k elements, and if the dist b/t first
        # and last is less than or equal to dist, it's valid 
        # otherwise, each of these elements that has been popped is a 
        # candidate to be the first valid index, and we need to track
        # how many of the other candidates so far are greater than this
        # one, but the difference being less than or equal to dist

        ### This doesn't work 
        # # heap = heapify([(-v, i + 1) for i, v in enumerate(nums[1:])])
        # heap = [(v, i + 1) for i, v in enumerate(nums[1:])]
        # heapify(heap)
        # # print(heap)
        # tally = [0] * len(nums)
        # valid = set()
        # while heap:
        #     _, i = heappop(heap)
        #     maxB = min(i + dist + 1, len(nums)) # maxB exclusive 
        #     tally[i] = 1 + sum([1 if tally[ix] else 0 for ix in range(i, maxB)]) 
        #     if tally[i] == k - 1: valid.add(i) # return nums[0] + sum([nums[ix] if tally[ix] else 0 for ix in range(i, maxB)])
        #     minB = max(i - dist, 0) # minB inclusive 
        #     for ib in range(minB, i):
        #         if tally[ib]: 
        #             tally[ib] += 1
        #             if tally[ib] == k - 1: valid.add(ib)
        #                 # maxB = min(ib + dist + 1, len(nums))
        #                 # return nums[0] + sum([nums[ix] if tally[ix] else 0 for ix in range(ib, maxB)])
        #     if valid:
        #         print(tally)
        #         return nums[0] + min([sum([nums[ix] if tally[ix] else 0 for ix in range(ibv, min(ibv + dist + 1, len(nums)))]) for ibv in valid])
        
        heap = []
        # chkpt = dist + 1
        # best = 10 ** 16
        # for i, v in enumerate(nums[1:]):
        #     if i == chkpt: 
                
        #     heappush(heap, (v, i))
        # for i, v in enumerate(nums[1:dist + 2]): heappush(heap, (v, i))
        # crits = sorted([heappop(heap) for _ in range(k - 1)], key=lambda x: x[1])
        crits = []
        # best = nums[0] + sum([x[0] for x in crits])
        best = 10 ** 16
        # chkpt = crits[0][1] + dist + 1
        chkpt = dist + 2
        # i = dist + 2
        i = 1
        while i <= len(nums):
            # if i == chkpt: # or chkpt >= len(nums):
            if (not crits and i == dist + 2) or (crits and i == crits[0][0] + dist + 1):
                while len(crits) < k - 1:
                    # crits.append(heappop(heap))
                    v, i = heappop(heap)
                    heappush(crits, (i, v))
                    best = nums[0] + sum([x[1] for x in crits])
                while heap[0][1] < crits[0][0]: # i - dist: 
                    heappop(heap)
                # crits.append(heappop(heap)) # before or after filling in crits on first chkpt ?? 
                v, i = heappop(heap)
                heappush(crits, (i, v))
                heappop(crits)
                # crits.sort(key=lambda x: x[1]) # i'm lazy, cause it's already sorted except for possibly the last element just added 
                # chkpt = min(crits[-(k - 2)][1] + dist + 1, len(nums))
                chkpt = min(crits[0][0] + dist + 1, len(nums))
                # best = min(best, nums[0] + sum([x[0] for x in crits[-(k - 1):]]))
                best = min(best, nums[0] + sum([x[1] for x in crits]))
                print(f"At chkpt {i}: crits={crits}; next chkpt={chkpt}; best={best}")
            if i == len(nums): break
            heappush(heap, (nums[i], i))
            i += 1
        return best

tests = [
    {
        "in": ([1,3,2,6,4,2], 3, 3),
        "out": 5
    },
    {
        "in": ([10,1,2,2,2,1], 4, 3),
        "out": 15
    },
    {
        "in": ([10,8,18,9], 3, 1),
        "out": 36
    },
    {
        "in": ([6,40,41,11,50,15,47,48,50,12,16,30,38,45,13,34,26,25,32,28], 9, 13),
        #      [0, 0, 0, 7, 0, 8, 0, 0, 0, 8, 7, 6, 0, 0, 5, 0, 4, 3, 2, 1]     # (6), 11, 15, 12, 16, 30, 13, 26, 25, 32, 28
        # Hmm, my solution doesn't actually work. The ideal solution begins with a partition at the 11 at index 3. 
        # We need to keep searching past the first minimum in order to find a way to use the 11, the benefit from using 
        # the smallest element is worth it more than the few points over the other minimums that the 34 adds 
        "out": 163
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        result = sol.minimumCost(*test["in"])
        assert result == test["out"], f"Expected {test["out"]}, got {result}"
    print("All tests passed.")