from typing import List
from math import inf
# from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        lookup = {originalLetter: {changedLetter: inf if changedLetter != originalLetter else 0 for changedLetter in letters} for originalLetter in letters}
        # brute force graph creation, not clever at all ... 
        # could use dirty/clean flags or something, or build an actual graph, not this pseudo fully connected web
        for originalLetter, changedLetter, changeCost in zip(original, changed, cost):
            if changeCost < lookup[originalLetter][changedLetter]:
                lookup[originalLetter][changedLetter] = changeCost
                for preOriginalLetter in letters:
                    for postChangedLetter in letters:
                        detourCost = lookup[preOriginalLetter][originalLetter] + changeCost + lookup[changedLetter][postChangedLetter]
                        lookup[preOriginalLetter][postChangedLetter] = min(lookup[preOriginalLetter][postChangedLetter], detourCost)
        ans = 0
        for charFrom, charTo in zip(source, target):
            if lookup[charFrom][charTo] == inf: return -1
            ans += lookup[charFrom][charTo]
        return ans
    
tests = [
    {
        "in": ("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]),
        "out": 28
    },
    {
        "in": ("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]),
        "out": 12
    },
    {
        "in": ("abcd", "abce", ["a"], ["e"], [10000]),
        "out": -1
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        result = sol.minimumCost(*test["in"])
        assert test["out"] == result, f"Expected {test["out"]}, got {result}"
    print(f"All tests passed.")