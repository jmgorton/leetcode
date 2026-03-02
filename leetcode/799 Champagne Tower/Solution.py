import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner

from functools import cache

class Solution:
    @cache
    def champagneTower(self, poured: float, query_row: int, query_glass: int) -> float:
        ### This is kind of a fibonacci problem mixed with an 
        # Euler-ish type of Sum(1, N)=N*(N+1)/2 problem.
        # it can be solved with math pretty quickly and easily
        # let's just do DP first, maybe...
        # this could also probably be easily solved with recursion
        # I'm going to do that first, since it seems so easy... 
        # nvm, maybe it's not 
        # maybe a better way to do this is to be able to quickly 
        # calculate when each glass will start to fill, 
        # and when each glass will be full. but that equation isn't
        # a constant slope, at some point during filling, the rate
        # of filling can double

        # So since there are 100 rows, and each row i has i glasses,
        # There are 100*101/2=50*101=5050 total glasses. 
        # The champagne poured down goes from glass i into glasses
        # Unlike a binary tree, each child has two parents,
        # and two neighbor glasses will pour into the same child
        # The n^th glass in a row will pour into the n^th and the n+1^th
        # glasses in the next row 
        # The 0th glass in row j is the {j*j+1/2}^th glass total 
        # the ith glass in row j (the kth total glass) will get poured 
        # into by the {k-j}^th total glass (unless j == i) and the 
        # {k-j-1}^th total glass (unless i == 0)

        if poured > 5050: return 1.0
        @cache
        def recur(poured: float, query_row: int, query_glass: int) -> float:
            if poured <= 0: return 0.0
            if query_glass < 0 or query_glass > query_row: return 0.0
            if query_row == 0: return min(1.0, poured)
            # poured - 1 is wrong. two parents filling this glass 
            return self.champagneTower((poured - 1) / 2, query_row - 1, query_glass) + self.champagneTower((poured - 1) / 2, query_row - 1, query_glass - 1)
        return recur(poured, query_row, query_glass) 
    

        ### Official solution:
        # Keep track of how much champagne flows through each glass with DP
        # dp = [[0] * k for k in range(1, 102)]
        # dp[0][0] = poured
        # for row in range(query_row + 1):
        #     for glass in range(row + 1):
        #         q = (dp[row][glass] - 1.0) / 2.0
        #         if q > 0:
        #             dp[row + 1][glass] += q
        #             dp[row + 1][glass + 1] += q
        
        # return min(1.0, dp[query_row][query_glass])

TEST_CASES = [
    # Input: poured = 1, query_row = 1, query_glass = 1, expected = 0.00000
    {"id": 1, "poured": 1, "query_row": 1, "query_glass": 1, "expected": 0.00000},
    # Input: poured = 2, query_row = 1, query_glass = 1, expected = 0.50000
    {"id": 2, "poured": 2, "query_row": 1, "query_glass": 1, "expected": 0.50000},
    {"id": 3, "poured": 100000009, "query_row": 33, "query_glass": 17, "expected": 1.0},
    {"id": 4, "poured": 25, "query_row": 6, "query_glass": 1, "expected": 0.1875},
    # == poured=12, query_row=5, query_glass=1 (left) + poured=12, query_row=5, query_glass=0 (right)
    # == poured=5.5, query_row=4, query_glass=1 (left left) 
    #       + poured=5.5, query_row=4, query_glass=0 (left right) 
    #       + poured=5.5, query_row=4, query_glass=0 (right left) ... + 0 (right right) 
    # == 
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="champagneTower",
        input_keys=["poured", "query_row", "query_glass"],
    )
    runner.run_tests()