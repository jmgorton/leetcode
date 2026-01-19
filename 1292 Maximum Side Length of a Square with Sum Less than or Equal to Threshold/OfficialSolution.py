# Key insight:

# Two-Dimensional Prefix Sums
# This problem requires knowledge of two-dimensional prefix sums, 
# which are an extension of one-dimensional prefix sums.
# The array P is the prefix sum array of A, where 
#   each element P[i][j] is defined as follows:
#   - If both i and j are greater than 0, then P[i][j] represents 
#       the sum of all elements in the rectangular region of A 
#       with the top-left corner at (1, 1) and the bottom-right 
#       corner at (i, j).
#   - If either i or j is equal to 0, then P[i][j] = 0.

# The prefix sum array P allows us to compute the sum of elements 
#   in any rectangular submatrix in O(1) time. Specifically, 
#   if the top-left corner of the rectangle is (x1, y1) and 
#   the bottom-right corner is (x2, y2), then the sum of elements 
#   in this region is:
#       sum = A[x1..x2][y1..y2] 
#       = P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

# Key Insight #2:

# Because all elements in mat are non-negative integers, 
#   an important monotonicity property holds:
#   If there exists a square with side length c whose sum 
#   does not exceed the threshold, then there must also exist 
#   valid squares of side lengths 1, 2, ..., c - 1. This is 
#   because any smaller square can be chosen inside the larger valid square.
# Since the sums of the squares are monotonically non-decreasing,
#   we can use binary search to find the largest square from 
#   a given corner in O(log N) time, where N is the length of max square,
#   the minimum of (i, j) for a point at mat[i][j] 

# Key Insight #3: (Optimization relevant to my strategy)

# If we have already found a valid square with side length c', 
# then for any subsequent top-left corner (i, j), there is no 
# need to check side lengths less than or equal to c'. We can 
# start directly from c' + 1.

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            find = any(
                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        r, ans = min(m, n), 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, r + 1):
                    if (
                        i + c - 1 <= m
                        and j + c - 1 <= n
                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
                    ):
                        ans += 1
                    else:
                        break
        return ans