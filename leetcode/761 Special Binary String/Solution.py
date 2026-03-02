import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # find the indices of special substrings 
        # a special substring can *never* end in a 1
        stack = [(0, 0)]
        # special = {}
        swapOpts = {} # [end index excl]: list of swappables
        for i, c in enumerate(s):
            if c == "1": 
                stack.append((stack[-1][0] + 1, i + 1))
            else:
                # while stack and stack[-1][0] > 
                bal, ib = stack.pop()
                while stack and stack[-1][0] == bal:
                    stack.pop()
                bal -= 1
                if stack:
                    ix = -1
                    if stack[ix][1] not in swapOpts: swapOpts[i + 1] = [s[stack[ix][1]:i + 1]]
                    else:
                        # print(swapOpts[stack[ix][1]])
                        # print([s[stack[ix][1]:i + 1]])

                        # swapOpts[i + 1] = swapOpts[stack[ix][1]] + [s[stack[ix][1]:i + 1]]
                        swapOpts[i + 1] = swapOpts[stack[ix][1]][:]
                        swapOpts[i + 1].append(s[stack[ix][1]:i + 1])
                        # don't delete the existing record...
                    # while -ix <= len(stack) and stack[ix][0] == bal:
                    #     if stack[ix][1] not in special: special[stack[ix][1]] = []
                    #     special[stack[ix][1]].append(i + 1) # ib
                    #     ix -= 1
                    stack.append((bal, i + 1))
                else:
                    stack.append((0, i + 1))
            # TODO simplify this logic... allow negative balance? 
            # but it works as expected for now 
        # print(special)
        print(swapOpts)

        # # traverse special graph to compare all swaps? 
        # # or rank special substrings and greedily apply positive swaps 
        # # i think it's not possible to create a new special substring
        # # by swapping two existing special substrings
        # # swapOpts = []
        # for k in special.keys():
        #     # ki = k
        #     # while s[ki] == "1": ki += 1
        #     for e in special[k]:
        #         if e not in special: continue
        #         # ei = e
        #         # while s[ei] == "1": ei += 1
        #         # gain = (ki - k) - (ei - e)
        #         # if gain <= 0: continue
        #         # swapOpts.append((gain, k, e))

        results = []
        for end, vs in swapOpts.items():
            if len(vs) == 1: continue
            start = end - sum([len(v) for v in vs])
            print(start, end)
            print(f"{vs} -> {sorted(vs, reverse=True)}")
            results.append(s[:start] + "".join(sorted(vs, reverse=True)) + s[end:])

        # result = s
        results.sort()
        print(results)

        return results[-1] if results else s
                    

# Test cases extracted from README
TEST_CASES = [
    {"id": 1, "s": "11011000", "expected": "11100100"},
    {"id": 2, "s": "10", "expected": "10"},
    {"id": 3, "s": "101101011000", "expected": "111001010010"}
]


if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="makeLargestSpecial",
        input_keys=["s"],
        debug=[3]
    )
    runner.run_tests()