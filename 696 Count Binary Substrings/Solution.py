import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner

from itertools import pairwise, groupby

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # for x, y in pairwise([(k, len(list(g))) for k, g in groupby(s)]):
        #     print(x, y)
        # return -1
        return sum([min(x) for x in pairwise([len(list(g)) for _, g in groupby(s)])])


# Test cases extracted from README
TEST_CASES = [
    {"id": 1, "s": "00110011", "expected": 6},
    {"id": 2, "s": "10101", "expected": 4},
]


if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="countBinarySubstrings",
        input_keys=["s"],
    )
    runner.run_tests()
