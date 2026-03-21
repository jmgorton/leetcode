from typing import List
from heapq import heappush, heappop

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # for each worker, let's put onto a heap
        # their expected task finish time (sort key),
        # and at what time it will complete the
        # following task, which will be the current time
        # plus that worker's initial time times that 
        # worker's next task number

        # that way we don't have to precompute for each
        # worker the time it would theoretically take
        # them to do a bunch of unnecessary work, like 
        # clearing the whole mountain themselves

        heap = []
        for i, wt in enumerate(workerTimes):
            heappush(heap, (wt, wt, 1))
        
        for _ in range(mountainHeight):
            et, wt, tn = heappop(heap)
            ntd = wt * (tn + 1)
            heappush(heap, (et + ntd, wt, tn + 1))
        
        return et