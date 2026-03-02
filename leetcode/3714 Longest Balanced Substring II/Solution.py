import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from TestRunner import TestRunner

from itertools import groupby

class Solution:
    def longestBalanced(self, s: str) -> int:
        # Same problem as the previous three days. 
        # Longest Balanced Subarray I & II, where we handled arrays of numbers,
        # and Longest Balanced Substring I, where we handled a string of lowercase letters.
        # In this problem, we only have three distinct characters, but the input is much larger.

        ### Hint 1: Solve for three cases: all-equal characters, exactly two distinct characters, 
        # and all three characters present. Treat each case separately and take the maximum length.

        ### Hint 2: Case 1: single character: the longest balanced substring is the longest run of 
        # the same character; report its length.

        ### Hint 3: Case 2: two distinct characters: reduce to that pair (ignore the third character) 
        # and use prefix differences of their counts; equal counts between two indices mean the 
        # substring between them is balanced for those two chars.

        ### Hint 4: Case 3: all three characters: use prefix counts and hash the pair 
        # (count_b - count_a, count_c - count_a) for each prefix; if the same pair appears at two 
        # indices the substring between them has equal counts for a, b, and c. Store earliest index 
        # per pair to get maximal length.

        ####### ******* ####### 

        # Case 1: Use groupby to find the longest run of a single character.
        groups = groupby(s)
        # if len(list(groups)) == 1: return len(s)
        best = [0, 0, 0]
        # best = [max([len(list(g)) for _, g in groupby(s)]), 0, 0]
        # excluded = {"a", "b", "c"}.difference({k for k, _ in list(groups)[:2]}).pop()
        excluded = {"a", "b", "c"}
        i = 0
        while i < len(s) and s[i] == s[0]: i += 1
        if i == len(s): return len(s)
        excluded = excluded.difference({s[0], s[i]}).pop()
        prev = None
        # count = 0
        counts = {"a": 0, "b": 0, "c": 0}
        for k, g in groups:
            # Case 1: single character
            c = len(list(g))
            best[0] = max(best[0], c)
            # Case 2: two characters
            if k == excluded:
                # best[1] = max(best[1], count)
                # count = prev[1] + c
                counts[prev[0]] = prev[1]
                counts[k] = c
                best[1] = max(best[1], min(counts[k], counts[prev[0]]))
                excluded = {"a", "b", "c"}.difference({k, prev[0]}).pop()
                counts[excluded] = 0
            else:
                # count += c
                counts[k] += c
                # if prev and counts[k] >= counts[prev[0]]:
                #     best[1] = max(best[1], counts[prev[0]] * 2)
                if prev: best[1] = max(best[1], min(counts[k], counts[prev[0]]) * 2)
            prev = (k, c)
        
        # Case 3: all three characters
        counts = {"a": 0, "b": 0, "c": 0}
        prev = {(0, 0): -1}
        for i, v in enumerate(s):
            counts[v] += 1
            key = (counts["a"] - counts["b"], counts["a"] - counts["c"])
            if key in prev: best[2] = max(best[2], i - prev[key])
            else: prev[key] = i

        # # Case 2 & Case 3: For each pair of characters, use prefix differences to find the longest balanced substring.
        # prefix = [[0, 0, 0]]
        # for v in s:
        #     prefix.append(prefix[-1][:])
        #     prefix[-1][ord(v) - ord('a')] += 1
        # for i in range(len(s) - best[0]):
        #     for j in range(i + best[0], len(s) + 1):
        #         if prefix[j][0] - prefix[i][0] == 0:
        #             if prefix[j][1] - prefix[i][1] == prefix[j][2] - prefix[i][2]:
        #                 best[1] = max(best[1], j - i)
        #         elif prefix[j][1] - prefix[i][1] == 0:
        #             if prefix[j][0] - prefix[i][0] == prefix[j][2] - prefix[i][2]:
        #                 best[1] = max(best[1], j - i)
        #         elif prefix[j][2] - prefix[i][2] == 0:
        #             if prefix[j][0] - prefix[i][0] == prefix[j][1] - prefix[i][1]:
        #                 best[1] = max(best[1], j - i)
        #         else:
        #             if prefix[j][0] - prefix[i][0] == prefix[j][1] - prefix[i][1] == prefix[j][2] - prefix[i][2]:
        #                 best[2] = max(best[2], j - i)
        print(best)
        return max(best)

# Test cases extracted from README
TEST_CASES = [
    {"id": 1, "s": "abbac", "expected": 4},
    {"id": 2, "s": "aabcc", "expected": 3},
    {"id": 3, "s": "aba", "expected": 2},
    {"id": 4, "s": "cbbacabbccaaaaaacbbbaabacbbcabbccbabbbbcaabccabaacbabcacccaccbabaaccbacbcbabaaaaaaacacccabaaacbcbcccabcbababbabccbccbacbbbabaaabaaabbaccccbbbacabcccccababcabbcaccacacbaaabccabacbaacaacbccaaaacaaabccbbaacacbacbcabbccabaaccbcbcaaccbabacbaacaaacbaaabcaabcbcbbcaabbbbacbbababaccbbbccbbaacaacbbccccccaacbabaacababbcabbaacbccabbcaaaaaccbcababbccccabbccaacbbccbbaaacabccccbcabacabababcbacbabcacacaabacbaabcaaaaaaababcbcbaaaacabcacbccbcbaaccbcabcacabaabbbabbaccacabbbabcaabbaababbaaaacacccaaabcabbacabacaaabcccaabccaacaccacbacabacbbababcacaaaacbbaabaacbbbabcaabaabbaaaccaccccaaccccacccbacbaabcaaacacaacabcbcccbcbabbababcbcbaccabbbbabcbbabccacaccbaaaaccbcaacabacbbbbccabbcaccababbbaacabcbcababbcbaaababaccacabacabcabaababcaabcccccbbacbccacabcbabcccabacbacccacabccbbbcccababbaaccbbcbbcaabcbccaaabaabcbbaaccaacbcbbbababaccbcaacbccaccaabcabbbabbacbabcacacaaabccbaaabacacaabcaccacaaacbbbaccbcacbbcaacacbcabacccccabbabcaabcbabbcccbccbccaabbbbbcabbabbaaabbcbcaacbbbbaabacaccbccbaabcbabcbcbccccccacccabccbabaccbbbbccbcabaccabaacbacacbbabbcaccbacbbcbcacbaabccaccbabaccbaacaaababbacabbbaaacbcbacccabcacaccbcbbcbabcaabacbabcbcabbbccacbabbbaaabbbbaabbcbbbbbabbbcaaabacabaccbaacbcaabcbcaacbbbabbbbacbabcaaaacbcccbaaaabbbbcabbaaabbcaabacbaaaaabbaaaabcbbcbcaacbcbbbabbaabacbacccbccbbccbcbaccbacabbabaaaacbbaaaaacbbabbbcbbacbcbbccbcbcaccaaacaccaaccbaacccabacaaaaccbaabbbbcaccaccacbcabbcccbbcbaaabbaabacbbbacaaccacccbbcbaacbcaacaccabaccacbcbabcbbccccccaccaacaaabacacaabbcacbcaabbaccbcbbbabbaacbcaabaaaabbbbabbbcaababbbbaaccbabccccacbbabccbcbccacabaaacbaccccabbacbbccccaccccaaaaaacbbabbacccbccbcaaabbcabbaccabbccbaabacabbbacacccaccabbccaccbaaabababbccbaabaababacbcbccbaabbaaaccccaaacccccabccaccabaabbaaabccbbcabbabccbcacbabacbacacbaaaaabbcabcbbaccccbacbcacbabaabcabcacabbbcaabaacbabcabbabaacccbabbbcbbbcccaccbbcaacccabbbcbacabbbbbaabcabcabbbabccaccbaabcaccaaacbabcbbaabcaccccbbbccabacabbccccabbccabcaacaacccbbbbcaccbaabcaaccbaaabcabcbbbcaabacccaabcabccbcabbaaabcbccaabcacccaabacbababaabccacbacabccbacaababacaccaaabcbbcbacccaaaabbcabccccbccbbbbacaccbcacbccbacbaccccaaccbacbbbbbbccabbbabbbbaaababbabbaacbcbccbcbbbaacaccbcacbbbbacbcbcabbcccbcaaccabccabbbaaacbabbbbaaabcccaabccbaabccacccbcaabcaabbbccacbacbbbcbabaaababacbcaaaaaacbcabbabbbccaccbcbabbaacabccacaaabbaccaccabbcccababbabaacbbcabacbcbbccbaaccbcccbbcacbcaaacabccbcccabccccbcacbbbabbcabaabccbcaaccabcaaacacbccabcccbbaacacbaabaacbcaabcbaccccacbbcaaccabbcccbbcbacbbcacbabcaccabbaacbaacbaaccaccaccacbcabbaacccbabbbcbcccbacacbccccaccbbbacbcaabacbaaabcbbbaaacababaabbbbaccbabacbcccabbcaccbabcabbcaccaaaccacbcbababaabacaabababccacbacacbccabbcacabbcabaaaaacbbacabaaccccbbbbbaabcaaaccccbcbcabccacabacbbcccbbcababbbacccaccabbccabccacabccbabbbabcbbacbbbacbacccbbcabbacbbcacabbbbcbbcacbcbcbaababbcbabaabaccbbcbcabbabbbbacaacccacccabcacbbabbaacbcbbcabbbbbcbccaccbcbacacbbbcccbbbcbcabcaabaaacbaabaabbcbbaabcbacaaaccbaaaccccabcbacacacaaaaabbccaaacaaabaaccaacbccbbcbcbcccabcccbcabbabccabaaabaaababccccaabbcaccaabbbabaaaccabccbaacacacccabababbccacbabcbccacacccbbabcbcbacaabababbbcaaabcaabbababaacbcbaaabcbabaabccbaacbcaabcaacacbbbcbbabacacbcacbbacccccabbabccbcaabbcbcbabbaabaccabaabbcaacccaabbbbbabbaabaccaaaaacbcccccabbbbaaccccacbbcacbccbbccbbbcbccbabbbbcaabbbbabbbacbbaaabaccacbabbabbcbcabbbbbcbcbcaaacacabcbbcbabbcbbcbacbbbcacccaaacaacbcbbabaacbbcbacaccbccaabcbaacabacabcaaaccbccbbcabcccbabcbbaabcccbcaaabcbcaaccabcbccaacbaaaaaaaaacbabacbbcaabcbabcaaaacaabcacbabbcccbcacabccabccbbaccaccaacbcccababcbaacaacbacbbababcbbacccccbcbbabbacaacaccabcacbbacacaabaaabccbabcbbaccbacabbbcaaaabccaabbbbabccbaabaaacbbcaacabbacaacaccbbbacbccababcbbaacacaaabcaacacababcabcabbbbbccaccbabaaacabbcbbbbbacbbbabccbcaaaaaaabaaabaccacacaccbcbbcbaaacbcaabbbcccacccacccacbaabababbbbcacccbbbabaccbcbbbaabbbbcbacccaabccabcaabcbacbbbabcacccabaaaacabcbbacbccacababcbaacabbabaaaabbbbbbaabcbccacbaacbaccaaabcaacbbccabcbaabbabccaacbbbccbcaaacaaaaabbcbaacacaaaccbabaaaaabcaaacbcaabccbbabcccbabaaaaabababcbcabbaaabccbcbabbcacbbbbcabacaabacaabcabaacacabcccacbbcccbccbcbccaacababbccaabcbbcccbbbabbabbcbccaacaaaccaccaaaccaaaaccaaaacababccbcbabbcbcaabacbaabcbbccbccacaacccaaabcbcccabacbcacbcbccabbabaaacaaacbabbccbcbcabccbabcacacbbbbacbacaaabccbcabacacbcccaabbabcabbcabbccabacbcbbccabcccbaabcaaaacccbbacbbcbbbccaccbccabaacbbacabaabbabaaabcabaabaacacbaaabbbbcaccbccbaabbbcaccbbcabaabcabaabbbbbbaacbbbacaabbacabbbcabaabbaabcccbccbabbbccaaccbbbacaccabacbccaabcabccaaaabbccaacbacccbaaacbccccccbbabaacbabaccbbaabcbcbcbcabcaaccabacaaacaaacbcabcbcbcabccaccccccbaabccbbabbccbaacbcbacacacaabcccbbcaacabaabccabcaaacbbbabbacaaaaabcbcaabaacabaccabcabcbccbaccbaaccbabcbacccacbcbacacaabacaaaccbacbacacbaabbcccabaabbabbcbbbaaacbaacccccccaabcbbbacbbaaacabaaaccacabaaacbabccacabbacacaccacccccabacbbaaaccaaa", "expected": 3471},
    {"id": 5, "s": "ccaca", "expected": 4},
    {"id": 6, "s": "cbbbc", "expected": 3},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="longestBalanced",
        input_keys=["s"],
    )
    runner.run_tests()