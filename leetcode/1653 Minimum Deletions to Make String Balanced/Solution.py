class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCountToRight = s.count('a')
        bCountToLeft = 0
        best = aCountToRight
        for c in s:
            if c == 'a': aCountToRight -= 1
            else: bCountToLeft += 1
            toRem = bCountToLeft + aCountToRight
            best = min(best, toRem)
        best = min(best, bCountToLeft)
        return best

tests = [
    {
        "in": "aababbab",
        "out": 2
    },
    {
        "in": "bbaaaaabb",
        "out": 2
    },
    {
        "in": "b",
        "out": 0
    },
    {
        "in": "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba",
        "out": 60
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        actual = sol.minimumDeletions(test["in"])
        assert actual == test["out"], f"Expected {test["out"]}, got {actual}"
    print("All tests passed")