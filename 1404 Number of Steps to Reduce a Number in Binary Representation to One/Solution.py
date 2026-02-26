class Solution:
    def numSteps(self, s: str) -> int:
        
        # pretty similar to the collatz conjecture, but easier 
        # instead of 3x+1 for odds, it's just x+1
        # the idea of this problem is to use str patterns,
        # not to convert to int and do math, which is 
        # possible in Python and similar languages w BigInt 
        # but not always possible in other languages, and 
        # defeats the purpose

        # groups of trailing 0s are counted, added to result, and chopped
        # groups of trailing 1s are all switched to 0s and the first 0 is
        # switched to a 1, and this happens in a single operation.
        # combining these two, if we ensure we have a trailing 1 group at
        # the end of the string at step 0, then we can count the size of 
        # the group g_s, add g_s + 1 to result, and chop g_s chars from 
        # the end of the string, then switch the new last char to a 1

        i = -1
        while s[i] == '0': i -= 1 # i >= -len(s) and # ... find first 1 (guaranteed to exist)
        result = -1 - i
        while i > -len(s):
            j = i - 1
            while j >= -len(s) and s[j] == '1': j -= 1
            result += i - j + 1
            i = j
        return result

import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner

TEST_CASES = [
    {"id": 1, "s": "1101", "expected": 6},
    {"id": 2, "s": "10", "expected": 1},
    {"id": 3, "s": "1", "expected": 0},
    {"id": 4, "s": "11", "expected": 3},
    {"id": 5, "s": "101", "expected": 5},
    {"id": 6, "s": "1111", "expected": 5},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="numSteps",
        input_keys=["s"],
        debug=True,
    )
    runner.run_tests()