from typing import List
# from functools import cache
from itertools import accumulate

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        # this is not a super efficient way to compute this, and...
        # @cache # should not speed this up at all 
        def maxSideLengthRecursive(self, mat: List[List[int]], threshold: int) -> int:
            if not mat: return 0
            # if len(mat) == 1 and len(mat[0]) == 1: return 0 if mat[0][0] > threshold else 1

        
    
        def maxSideLengthIterativeV1(mat: List[List[int]], threshold: int) -> int:
            # if not mat or len(mat) == 0: return 0

            colSums = []
            rowSums = []
            for iy, row in enumerate(mat):
                colSums.append([])
                rowSums.append([])
                for ix, el in enumerate(row):
                    if el <= threshold: 
                        colSums[iy].append([el])
                        rowSums[iy].append([el])
                        if iy > 0:
                            for prevEl in colSums[iy - 1][ix]:
                                if prevEl + el > threshold: break
                                colSums[iy][ix].append(prevEl + el)
                        if ix > 0:
                            for prevEl in rowSums[iy][ix - 1]:
                                if prevEl + el > threshold: break
                                rowSums[iy][ix].append(prevEl + el)

            maxSideLength = 0
            squareSums = []
            # squareSums = [[[] for _ in range(len(mat[0]))] for _ in range(len(mat))]
            for iy, row in enumerate(mat):
                squareSums.append([])
                for ix, el in enumerate(row):
                    squareSums[iy].append([])
                    sizeOfSquare = 0
                    squareSum = el
                    while squareSum <= threshold:
                        squareSums[iy][ix].append(squareSum)
                        if ix and iy and sizeOfSquare < min(len(squareSums[iy - 1][ix - 1]), len(rowSums[iy][ix - 1]), len(colSums[iy - 1][ix])):
                            # el += squareSums[iy - 1][ix - 1][sizeOfSquare] + rowSums[iy][ix - 1][sizeOfSquare] + colSums[iy - 1][ix][sizeOfSquare]
                            squareSum = el + squareSums[iy - 1][ix - 1][sizeOfSquare] + rowSums[iy][ix - 1][sizeOfSquare] + colSums[iy - 1][ix][sizeOfSquare]
                        else: break
                        sizeOfSquare += 1
                    maxSideLength = max(maxSideLength, len(squareSums[iy][ix]))

            return maxSideLength

        def maxSideLengthIterative(mat: List[List[int]], threshold: int) -> int:
            rowSums = []
            colSums = []
            maxSideLength = 0
            for iy, row in enumerate(mat):
                rowSums.append(list(accumulate(row))) # default behavior: operator.add 
                if iy: colSums.append(list(map(lambda x, y: x + y, row, colSums[iy - 1])))
                else: colSums.append(row)
                for ix, el in enumerate(row):
                    sideLength = 0
                    while el <= threshold:
                        sideLength += 1
                        if min(ix, iy) < sideLength: break
                        el += rowSums[iy - sideLength][ix] - rowSums[iy - sideLength][ix - sideLength]
                        el += colSums[iy][ix - sideLength] - colSums[iy - sideLength][ix - sideLength]
                        el += mat[iy - sideLength][ix - sideLength]
                    maxSideLength = max(maxSideLength, sideLength)
            
            return maxSideLength

        return maxSideLengthIterative(mat, threshold)
    
test1: dict = {
    'args': [
        [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],
        4
    ],
    'expected': 2
}

test2 = {
    'args': [
        [[14,69,73,53,64,25,46,71,51,99,83,55],
         [58,83,36,15,21,1,23,57,16,14,71,18],
         [90,17,67,59,15,100,82,39,81,36,91,52],
         [88,61,31,64,53,55,47,34,36,95,86,8],
         [49,24,68,76,47,9,83,97,11,70,26,60],
         [68,15,88,81,91,94,72,53,38,6,7,39],
         [45,54,29,90,61,47,68,67,40,64,10,85],
         [93,13,62,27,88,30,65,54,15,74,22,3],
         [8,96,10,45,5,97,44,18,43,84,1,57],
         [94,21,67,25,78,36,100,92,73,53,88,71],
         [69,43,53,12,63,64,61,25,24,3,95,33],
         [34,73,38,42,44,55,80,75,20,96,98,13],
         [90,79,22,82,6,30,3,34,72,10,37,84],
         [29,90,31,83,30,89,88,62,75,13,14,48],
         [11,66,46,84,28,51,47,55,52,74,61,43]],
        90212
    ],
    'expected': 12
}

test3 = {
    'args': [
        [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]],
        6
    ],
    'expected': 3
}

tests = [test1, test2, test3]

if __name__ == "__main__":
    sol = Solution()
    testsPassed = 0
    for i, test in enumerate(tests):
        if test['expected'] != (actual := sol.maxSideLength(*test['args'])):
            print(f"Fail: Test {i}: Expected {test['expected']}; Got {actual}")
        else:
            # print(f"Result {actual} is correct.")
            testsPassed += 1
    print(f"{testsPassed} / {len(tests)} Passed")
