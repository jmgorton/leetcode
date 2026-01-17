from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # ideas
        # each point stores quadrants with other points... bad 
        # segment tree ... 

        # hint 1: Brute Force the intersection area of each pair of rectangles.

        # wow, wasn't expecting that for hint 1...
        # i should have thought to start by attempting to implement a 
        # brute force approach when lacking better ideas 

        # brute force approach

        def getSideLengthOfLargestSquareInTwoRectanglesOverlap(rect1: List[int], rect2: List[int]) -> int:
            # each rectangle passes in 4 points: [leftX, bottomY, rightX, topY]
            # xOverlap: int
            # could do if rect2[0] < rect1[0]: rect1, rect2 = rect2, rect1 to guarantee
            # that rect1 is the left-most rectangle, but let's try to avoid var reassignment
            # if rect1[2] <= rect2[0]: xOverlap = 0
            # elif rect1[0] >= rect2[2]: xOverlap = 0
            # else: 
            xOverlap = min(rect1[2] - max(rect1[0], rect2[0]), rect2[2] - max(rect1[0], rect2[0]))
            if xOverlap < 0: xOverlap = 0
            yOverlap = min(rect1[3] - max(rect1[1], rect2[1]), rect2[3] - max(rect1[1], rect2[1]))
            if yOverlap < 0: yOverlap = 0
            return min(xOverlap, yOverlap)

        n = len(bottomLeft) 
        if n != len(topRight): return -1
        longestSideLength = 0
        for i in range(n):
            for j in range(i + 1, n):
                longestSideLength = max(
                    longestSideLength, 
                    getSideLengthOfLargestSquareInTwoRectanglesOverlap(
                        [*bottomLeft[i], *topRight[i]], 
                        [*bottomLeft[j], *topRight[j]]
                    )
                )
        
        return longestSideLength