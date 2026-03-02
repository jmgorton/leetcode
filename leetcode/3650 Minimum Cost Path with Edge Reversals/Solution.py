from typing import List
from math import inf
from collections import defaultdict

import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # graph = {x: {} for x in range(n)}
        # revGraph = {x: {} for x in range(n)}
        # from0 = [inf] * n
        # toEnd = [inf] * n
        # # from0[0] = 0
        # # toEnd[n - 1] = 0
        # for u, v, w in edges:
        #     graph[u][v] = w # can there be multiple edges between the same two nodes? 
        #     revGraph[v][u] = w
        # queue = [(0, 0)]
        # # queue = [(inf, x) for x in range(1, n)] # make sure all nodes calc'd even if disjointed graph ... this won't work
        # # heapq.heappush((0, 0))
        # while queue:
        #     dist0, node = heapq.heappop(queue)
        #     if dist0 > from0[node]: continue
        #     from0[node] = dist0
        #     # if node == n - 1: break # no actually, keep building whole graph 
        #     for v, w in graph[node].items():
        #         heapq.heappush(queue, (dist0 + w, v))
        # queue.clear()
        # queue = [(0, n - 1)]
        # while queue:
        #     distEnd, node = heapq.heappop(queue)
        #     if distEnd > toEnd[node]: continue
        #     toEnd[node] = distEnd
        #     for v, w in revGraph[node].items():
        #         heapq.heappush(queue, (distEnd + w, v))
        # result = from0[n - 1]
        # for u, v, w in edges:
        #     result = min(result, from0[v] + toEnd[u] + (2 * w))
        # return result if result < inf else -1
    
        ### i misunderstood the problem, this is how you do it if you can reverse at most one edge in the whole graph 
        ### but the actual problem allows reversing any number of edges, not just one
        ### each edge can be reversed at most one time, which is kind of a trivially obvious constraint
        ### there's no scenario where you would need to reverse an edge more than once

        graph = {x: defaultdict(lambda: inf) for x in range(n)}
        for u, v, w in edges:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], 2 * w)
        queue = [(0, 0)]
        best0 = [inf] * n
        best0[0] = 0
        while queue:
            dist, node = heapq.heappop(queue)
            if dist > best0[node]: continue
            best0[node] = dist
            if node == n - 1: break # now we actually can use this early term
            for v, w in graph[node].items():
                heapq.heappush(queue, (dist + w, v))
        if best0[n - 1] < inf: return best0[n - 1]
        return -1

tests = [
    {
        "in": (4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]),
        "out": 5
    },
    # {
    #     "in": (3, [[0,1,1],[1,2,1],[2,0,1]]),
    #     "out": 2
    # },
    {
        "in": (4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]),
        "out": 3
    },
    {
        "in": (3, [[2,1,1],[1,0,1],[2,0,16]]),
        "out": 4
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        inp = test["in"]
        expected = test["out"]
        result = sol.minCost(*inp)
        print(f"Input: {inp}, Expected: {expected}, Got: {result}, Pass: {result == expected}")