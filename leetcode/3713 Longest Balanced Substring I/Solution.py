from typing import List
import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner


class Solution:
    def longestBalanced(self, s: str) -> int:
        ### This is exactly the same problem as the previous two days
        # but instead of an input array of numbers between 1-100,000,
        # and comparing two cases: odd and even, we have a string of 
        # lowercase letters, so 26 cases to compare. 

        ### Yesterday's official solution approach was a prefix sum
        # in combination with a segment tree. Here's the snippet of
        # the solution editorial that i still don't understand:
        #   More generally, for a fixed left boundary, the right 
        #   boundary of the longest balanced subarray corresponds 
        #   to the rightmost position where the prefix sum is equal 
        #   to the prefix sum at the left boundary.
        # But based on the test cases that failed in my first approach,
        # i don't see how this is true. Because we're counting *distinct* 
        # characters (or odds/evens), consider the input [10,6,10,7]
        # then the prefix sums for balance are [1,2,2,1] ... the 
        # longest balanced subarray here is [10,7]. It does not matter
        # how many 6s appear, e.g. [10,6,6,6,6,10,7] achieves a 
        # transformed array of [1,2,2,2,2,2,1], and the answer is still
        # 2 ([10,7]). 

        ### The input on this problem is small enough that once again,
        # brute force will work. Let's do that first. 

        best = 1
        for i in range(len(s)):
            c = {}
            for j in range(i, len(s)):
                if s[j] not in c: c[s[j]] = 0
                c[s[j]] += 1
                if all([x == c[s[j]] for x in c.values()]): best = max(best, j - i + 1)
        return best


# Test cases extracted from README
TEST_CASES = [
    {"id": 1, "s": "abbac", "expected": 4},
    {"id": 2, "s": "zzabccy", "expected": 4},
    {"id": 3, "s": "aba", "expected": 2},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="longestBalanced",
        input_keys=["s"],
    )
    runner.run_tests()
