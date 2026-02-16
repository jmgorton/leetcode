import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner

class Solution:
    def reverseBits(self, n: int) -> int:
        # result = 0
        # print(f"{n:b}")
        # while n:
        #     result <<= 1
        #     result |= n & 1
        #     n >>= 1
        # print(f"{result:b}")
        # return result
        return int(f"{n:032b}"[::-1], 2)

TEST_CASES = [
    {"id": 1, "n": 43261596, "expected": 964176192},
    {"id": 2, "n": 2147483644, "expected": 1073741822}
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="reverseBits",
        input_keys=["n"],
    )
    runner.run_tests()