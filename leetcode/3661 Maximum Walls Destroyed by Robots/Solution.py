from typing import List
from heapq import heappush, heappop

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        roboHeap = []
        for pos, dist in zip(robots, distance):
            heappush(roboHeap, (pos, dist))
        walls.sort()

        best = [0, 0] # if prev robo aimed left/right
        boundary = [0, 0] # prevRobo position (if left), 
            # or prevRobo position + distance (if right) 
        
        while roboHeap:
            pos, dist = heappop(roboHeap)
            # llwb = 
