class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        pass 

        # follow up on yesterday's problem, with better math skills 
        # and we can precompute all the possibly necessary factorials mod 1e9 + 7 

        # total ways to arrange = n! / zero! one! (not caring about violations of limit) 
        # number of zeroes left after a violation streak of zeroes: zl1 
        # number of ones left after a violation streak of ones: ol1
        # total length of subarray on right side after a streak occurs at position i = 1..n: nli

        # number of ways that violate the limit with a streak from index 0 
        # 0! nl1! / zl1! one! + 0! nl1! / zero! ol1! (streak of 0s or 1s respectively) 

        # number of ways that violate the limit with a streak that starts at index 1 
        # nl2! / zl1! (one - 1)! + nl2! / (zero - 1)! ol1! (streak of 0s or 1s respectively)
        # note that the first character is predetermined as the opp of the streak, 
        # so we have one less of that char to work with here, but in general, we only care 
        # that the entire prefix prior to index 1 is stable, *and* the last character is an opp 

        # number of ways that violate the limit with a streak that starts at index i
        # for i in range 1 ... n - limit - 1 (can't have a streak that violates limit start after index n - limit - 1) 
        # and 2 is the index where it gets a little more complicated, because we have to make sure that the prefix prior to index i is stable,
        # and the last character of that prefix is an opp to the streak starting at index i
        # which affects how many 0s and 1s we have left to apply to the right side of the streak 
        # so for i = 2, the characters from i = 1 to i = limit + 1 are predetermined
        # but that leaves a left side of length 1 for which we have to test every combo of 0s and 1s
        # and reflect that on the right side of the array as well for the total number of possible arrangements 

        # so for i = 2, we have to test j = 0 and j = 1, which are the number of 0s we use on the left side of the array prior to index i
        # in this case, it means that unless the limit is 1, we have to multiply the previous calculation by 2
        # another way to calculate is to recurse, the formula:
        # WRONG: recur(0, 1, limit) * nl3! / zl1! (one - 2)! + recur(1, 0, limit) * nl3! / (zero - 2)! ol1! 
        # this approach is too complicted... it turns out we may actually have to cut the recursive portion 
        # in half because half of valid solution will end in the wrong character, but that depends on the limit 

        ### *** ### 

        ### Hint 1: Let dp[x][y][z = 0/1] be the number of stable arrays with exactly 
        # x zeros, y ones, and the last element is z. (0 or 1). dp[x][y][0] + dp[x][y][1] is the answer for given (x, y).

        ### Hint 2: If we have already placed x 1 and y 0, if we place a group of k 0, 
        # the number of ways is dp[x-k][y][1]. We can place a group with size i, where i varies 
        # from 1 to min(limit, zero - x). Similarly, we can solve by placing a group of ones.

        ### Hint 3: Speed up the calculation using prefix arrays to store the sum of dp states.


