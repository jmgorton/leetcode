from itertools import groupby
# from functools import cache

### Hint 1: Note what actually matters is how many 0s and 1s are in odd and even positions

### Hint 2: For every cyclic shift we need to count how many 0s and 1s are at each parity 
# and convert the minimum between them for each parity

class Solution:
    # @cache
    def minFlips(self, s: str) -> int:
        # c = sum(s[i] != s[i + 1] for i in range(len(s) - 1))
        #     return 0

        # heap = [] (# of violations, string, index to flip)

        # Before checking the official solution, using the editorial hints
        # Prefix sum + postfix sum
        # Another way to think about the cyclic shift is that we want 
        # to use type 2 operations to get at most one violation of the alternating pattern,
        # if the length of the string is odd. If even, we can accept no violations. 

        # prefixFlips = [(0, 0)]
        prefix = [[0, 0]]
        for i, c in enumerate(s):
            # prefixFlips.append((prefixFlips[-1][0] + ((i & 1) ^ int(c)), prefixFlips[-1][1] + 0 if ((i & 1) ^ int(c)) else 1))
            prefix.append(prefix[-1][:])
            if ((i & 1) ^ int(c)): prefix[-1][1] += 1 # flips to get substring from start to here to alternate starting with 1
            else: prefix[-1][0] += 1 # flips "" starting with 0 
        
        if not len(s) & 1: return min(prefix[-1])
        # return min([min(prefix[i][0] + prefix[-1][1] - prefix[i][1], prefix[i][1] + prefix[-1][0] - prefix[i][0]) for i in range(len(s) + 1)])
        print(prefix) 
        # return min([min(prefix[i][0] + prefix[-1][0] - prefix[i][0], prefix[i][1] + prefix[-1][1] - prefix[i][1]) for i in range(len(s) + 1)])
        return min([min(prefix[i][0] + prefix[-1][(i & 1)] - prefix[i][(i & 1)], prefix[i][1] + prefix[-1][(i & 1) - 1] - prefix[i][(i & 1) - 1]) for i in range(len(s) + 1)])
        # pass

        # # Can use recursion and caching 
        # # Iteration should also be relatively straightforward 
        # # We need to focus on groups of like characters 
        # # Might be a more clever way, but I think the 
        # # simplest way is to keep track of the best 
        # # result we can achieve on a group if the preceding 
        # # character was a "0" and if it was a "1" 
        
        # # Scenarios: 
        # # A: group of length 1
        # #   A1: s = "00100" -> 2
        # #   A2: s = "0001000" -> 2
        # #   A3: s = "000010000" -> 4
        
        # best = [0, 0]
        # # curr = [0, 0]
        # for k, g in groupby(s):
        #     lg = len(list(g))
        #     # if k == '1':
        #     #     # TODO opt with divmod? 
        #     #     bitsFlippedIf0Preceded = lg // 2
        #     #     willEndIn0If0Preceded = lg % 2 == 0
        #     #     bitsFlippedIf1Preceded = (lg + 1) // 2 # = bitsFlippedIf0Preceded + 1 if willEndIn0If0Preceded else bitsFlippedIf0Preceded 
        #     #     # willEndIn0If1Preceded = lg % 2 == 1 # not necessary, always not willEndIn0If0Preceded 
        #     #     newBest = [best[0] + bitsFlippedIf0Preceded, best[1] + bitsFlippedIf1Preceded]
        #     #     best = newBest if willEndIn0If0Preceded else newBest[::-1]
            
        #     bitsFlippedIfOppLedIn, willEndingsFlip = divmod(lg, 2)
        #     # bitsFlippedIfLikeLedIn = bitsFlippedIfOppLedIn
        #     # if willEndingsFlip: bitsFlippedIfLikeLedIn += 1
        #     best = [x + bitsFlippedIfOppLedIn for x in best]
        #     if willEndingsFlip:
        #         best[0 if k == '0' else 1] += 1
        #         best = best[::-1]
        # return min(best)

# Test cases based on the scenarios above and the 1888 README:
# Uses the pattern of the TestRunner 
# s = "00100" -> 2
# s = "0001000" -> 2
# s = "000010000" -> 4
# s = "111000" -> 2
# s = "0100" -> 1

from leettest import TestRunner

TEST_CASES = [
    {"id": 1, "s": "00100", "expected": 2},
    {"id": 2, "s": "0001000", "expected": 2},
    {"id": 3, "s": "000010000", "expected": 4},
    {"id": 4, "s": "111000", "expected": 2},
    {"id": 5, "s": "0100", "expected": 1},
    {"id": 6, "s": "01001001101", "expected": 2},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="minFlips",
        input_keys=["s"],
        debug=True,
    )
    runner.run_tests()