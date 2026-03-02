from heapq import *
from typing import List

# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         # Example 2:
#         # At y=0: A=0
#         # At y=1: A=2
#         # At y=2: A=5
#         # Split happens at 2.5 per side
#         # Starting at y=1 and going to y=2...
#         #   gain 3sq per 1y traveled 
#         #   want to gain 0.5sq
#         #   travel 0.5/3 above y=1
#         # Result: y=1.16667 (y=7/6) 

#         minHeapOfBottomEdges = []
#         minHeapOfTopEdges = []
#         totalArea = 0
#         for (x, y, l) in squares:
#             heappush(minHeapOfBottomEdges, (y, l))
#             heappush(minHeapOfTopEdges, (y + l, l))
#             totalArea += (l ** 2)
#         velocity = 0
#         areaUnderX2, nextAreaUnderX2 = 0
#         thisY, nextY, thisL = 0
#         while minHeapOfBottomEdges and minHeapOfTopEdges:
#             if minHeapOfBottomEdges[0][0] < minHeapOfTopEdges[0][0]:
#                 # new square starts
#                 nextY, thisL = heappop(minHeapOfBottomEdges)
#             elif minHeapOfBottomEdges[0][0] >= minHeapOfTopEdges[0][0]:
#                 # existing square ends 
#                 nextY, thisL = heappop(minHeapOfTopEdges)
#                 thisL = -thisL
#             diffY = nextY - thisY
#             nextAreaUnderX2 = areaUnderX2 + (diffY * velocity * 2)
#             if nextAreaUnderX2 > totalArea:
#                 # critical point is between thisY and nextY
#                 frac = (totalArea - areaUnderX2) / (nextAreaUnderX2 / areaUnderX2)
#                 return thisY + (diffY * frac)
#             elif nextAreaUnderX2 == totalArea:
#                 # nextY is the critical point
#                 return nextY
#             else:
#                 # critical point comes sometime after nextY
#                 areaUnderX2 = nextAreaUnderX2
#                 thisY = nextY
#                 velocity += thisL

# # Got this far and realized I don't need two separate heaps

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        edges = []
        totalArea = 0
        for (_, yi, li) in squares:
            heappush(edges, (yi, li)) # bottom edge, gaining area velocity of increase
            heappush(edges, (yi + li, -li)) # top edge, losing area velocity of increase
            totalArea += (li ** 2)
        
        velocity = posY = 0
        areaX2 = nextAreaX2 = 0
        while edges:
            y, l = heappop(edges)
            diffY = y - posY
            nextAreaX2 = areaX2 + (diffY * velocity * 2)
            if nextAreaX2 > totalArea:
                frac = (totalArea - areaX2) / (nextAreaX2 - areaX2)
                return posY + (diffY * frac)
            if nextAreaX2 == totalArea:
                return y
            posY = y
            areaX2 = nextAreaX2
            velocity += l
            while edges and edges[0][0] == y:
                _, l = heappop(edges)
                velocity += l

        return -1