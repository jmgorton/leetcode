from itertools import groupby, pairwise

class Solution:
    def binaryGap(self, n: int) -> int:
        # SIMPLE, WORKS 
        # prevBit = None
        # currBit = 0
        # mask = 1
        # best = 0
        # while mask <= n:
        #     if mask & n:
        #         if prevBit is not None: best = max(best, currBit - prevBit)
        #         prevBit = currBit
        #     mask <<= 1
        #     currBit += 1
        # return best 
                
        print(f"{n:b}")
        # print([(k, g) for k, g in groupby(f"{n:b}")])
        # print([x if x[0][0][0] == '1' else None for x in pairwise([x for x in pairwise([(k, len(list(g))) for k, g in groupby(f"{n:b}")])])])
        print(max(([x[0][1][1] if x[0][0][0] == '1' else x[0][0][1] for x in pairwise([x for x in pairwise([(k, len(list(g))) for k, g in groupby(f"{n:b}")])])]), default=-1) + 1) 
        return max(([x[0][1][1] if x[0][0][0] == '1' else x[0][0][1] for x in pairwise([x for x in pairwise([(k, len(list(g))) for k, g in groupby(f"{n:b}")])])]), default=-1) + 1

        # best = None
        
        # for k, g in groupby(f"{n:b}"):
        #     if k == "1":


# import sys
# sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
# from TestRunner import TestRunner

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from TestRunner import TestRunner

### Or, better long term: 
# Make repo/package structure explicit (__init__.py), 
# then run as module, and import via package path, e.g.
# from leetcode.TestRunner import TestRunner

TEST_CASES = [
    {"id": 1, "n": 22, "expected": 2},
    {"id": 2, "n": 8, "expected": 0},
    {"id": 3, "n": 5, "expected": 2},
    {"id": 4, "n": 6, "expected": 1},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="binaryGap",
        input_keys=["n"],
        debug=True
    )
    runner.run_tests()