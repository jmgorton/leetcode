from typing import List

### Hint 1: For each row of the grid, calculate 
# the most right 1 in the grid in the array maxRight.

### Hint 2: To check if there exist answer, sort 
# maxRight and check if maxRight[i] ≤ i for all possible i's.

### Hint 3: If there exist an answer, simulate the swaps.

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        max_right = []
        for row in grid:
            i = len(row) - 1
            while i > -1 and row[i] == 0: i -= 1
            max_right.append(i)
        
        if not all([x <= i for i, x in enumerate(sorted(max_right))]): return -1

        def recur(ladder: List[int]) -> int:
            for i, v in enumerate(ladder):
                if v > i:
                    # ladder[i], ladder[i + 1] = ladder[i + 1], ladder[i]
                    # ladder = ladder[:i] + ladder[i + 1:v] + [ladder[i]] + ladder[v:]
                    v = i + 1 # NOTE: this is important, we don't actually care about making sure
                        # this element is in the right place, we actually want to find the closest 
                        # element that is right *for this place*
                        
                    while ladder[v] > i: v += 1 # v < len(ladder) and ... not necessary bc we know a valid solution exists 
                    # ladder = ladder[:i] + [ladder[v]] + ladder[i + 1:v] + [ladder[i]] + ladder[v + 1:]
                    ladder = ladder[:i] + [ladder[v]] + ladder[i:v] + ladder[v + 1:]
                    ans = recur(ladder) + v - i
                    print(f"Adding {v - i} to score after swapping indices {i} and {v} in {ladder}. New score: {ans}")
                    return ans
            print("Returning score of 0, found valid solution")
            return 0
                
        print(f"Initial: {max_right}")
        return recur(max_right)
    
from leettest import TestRunner

test_cases = [
    {"id": 1, "expected": 3, "grid": [[0,0,1],[1,1,0],[1,0,0]]},
    {"id": 2, "expected": -1, "grid": [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]},
    {"id": 3, "expected": 0, "grid": [[1,0,0],[1,1,0],[1,1,1]]},
]

runner = TestRunner(test_cases, Solution, "minSwaps", ["grid"], debug=[1])
runner.run_tests()