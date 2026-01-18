import Solution

grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
expected = 3

runner = Solution.Solution()
actual = runner.largestMagicSquare(grid)
if actual == expected: print("Successful execution.")
else: print(f"Expected {expected}; got {actual}")