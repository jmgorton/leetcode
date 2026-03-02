from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ### First attempt 
        # distinctEven = set()
        # # evens = defaultdict(int) # {}
        # distinctOdd = set()
        # # odds = defaultdict(int) # {}
        # # distinct = [] # (even, odd) # could also use pos -> more even, neg -> less even 
        # prev = {0: -1} # distinct to first i lookup
        # best = 0
        # for i, v in enumerate(nums):
        #     if v % 2: 
        #         distinctOdd.add(v)
        #         # odds[v] += 1
        #     else: 
        #         distinctEven.add(v)
        #         # evens[v] += 1
        #     balance = len(distinctEven) - len(distinctOdd)
        #     # balance = 0
        #     # for key in evens.keys(): 
        #     #     if evens[key] > 0 and key not in odds or odds[key] == 0: balance += 1
        #     # for key in odds.keys():
        #     #     if odds[key] > 0 and key not in evens or evens[key] == 0: balance -= 1
        #     if balance not in prev: prev[balance] = i
        #     else: 
        #         # best = max(best, i - prev[balance]) # not necessarily, see [6,6] (test case 4) 
        #         # let's consider this an indicator of a *possible* solution, we have to verify
        #         verifyDistinctEven = {x if x % 2 == 0 else None for x in nums[prev[balance]+1:i+1]}
        #         verifyDistinctOdd = {x if x % 2 == 1 else None for x in nums[prev[balance]+1:i+1]}
        #         verifyDistinctEven.discard(None)
        #         verifyDistinctOdd.discard(None)
        #         if len(verifyDistinctEven) == len(verifyDistinctOdd): best = max(best, i - prev[balance])
        # return best 

        ### Second attempt 
        # insight: every balanced subarray is potentially a chain of contiguous balanced subarrays
        # we don't want to check if balance is in the previously seen dict
        # we want to subtract current balance from the previously seen balance and verify the result is 0
        # i want a way to hash a dictionary, i don't want to store the whole dictionary... 
        # i'm sure there's a better way to do this. the "optimal" solution might be O(n^2)...
        # or maybe we can use the input List somehow 
        # wait, maybe this can be a sliding window problem...?? 

        # when we encounter a new number, it's either a duplicate or a new distinct value
        # if it's a duplicate, the balance isn't changed
        # if it was balanced before, it remains balanced
        # if it's a new distinct value, the balance changes by 1 (even) or -1 (odd)
        # if we encounter a new distinct value that increases the balance,
        # we can check the last time the balance decreased by 1... no, oof 
        # ugh, the lc official solution is brute force. ugly 

        # # evens = set()
        # # odds = set()
        # best = 0
        # for i in range(len(nums)):
        #     odds = set()
        #     evens = set()
        #     for j in range(i, len(nums)):
        #         # evens = {x if not x % 2 else None for x in nums[j:i+1]}
        #         # odds = {x if x % 2 else None for x in nums[j:i+1]}
        #         if nums[j] % 2: odds.add(nums[j])
        #         else: evens.add(nums[j])
        #         # evens.discard(None)
        #         # odds.discard(None)
        #         if len(evens) == len(odds): best = max(best, j - i + 1)
        # return best
    
        ### Community solution
        # this is more or less what i was trying to do... smh 
        # wait, this is still O(n^2), i'm not sure how it's so fast... 
        best = 0
        balance = tuple([set(), set()])
        while len(nums) > best:
            balance[0].clear(); balance[1].clear()
            for r, x in enumerate(reversed(nums), start=1):
                balance[x & 1].add(x)
                if len(balance[0]) == len(balance[1]):
                    best = max(best, r)
            nums.pop()
        return best

tests = [
    {
        "in": [2,5,4,3],
        "out": 4
    },
    {
        "in": [3,2,2,5,4],
        "out": 5
    },
    {
        "in": [1,2,3,2],
        "out": 3
    },
    {
        "in": [6,6],
        "out": 0
    },
    {
        "in": [10,6,10,7],
        "out": 2
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        assert (actual := sol.longestBalanced(test["in"])) == test["out"], f"Expected {test["out"]}, got {actual}"
    print("All tests passed.")