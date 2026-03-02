from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        return 
    
from leettest import TestRunner

test_cases = [
    {"id": 1, "expected": 3, "grid": [[0,0,1],[1,1,0],[1,0,0]]},
    {"id": 2, "expected": -1, "grid": [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]},
    {"id": 3, "expected": 0, "grid": [[1,0,0],[1,1,0],[1,1,1]]},
]

runner = TestRunner(test_cases, Solution, "minSwaps", ["grid"], debug=True)
runner.run_tests()