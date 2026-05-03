from typing import List
from heapq import heappush, heappop

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # each square built up from bottom right up and to the left
        # computes a list of best scores associated with costs
        # sorted from min cost ascending (or sorted by best cost... nah)
        # and capped at k cost 

        # hmm, let's actually do a searching algorithm instead
        # something like djikstra based on best score 

        # description leaves ambiguous whether square (0,0) counts 
        # assume it does i guess ... nvm constraints do answer that 

        queue = [(0, 0, 0, 0)] # queue contains (-score, cost x, y) as a heap 
        while queue:
            invScore, cost, x, y = heappop(queue) 
            invScore -= grid[y][x]
            cost += 1 if grid[y][x] else 0
            if cost > k: continue
            if x == len(grid[0]) - 1 and y == len(grid) - 1: return -invScore
            if x < len(grid[0]) - 1:
                heappush(queue, (invScore, cost, x + 1, y))
            if y < len(grid) - 1:
                heappush(queue, (invScore, cost, x, y + 1))
        return -1