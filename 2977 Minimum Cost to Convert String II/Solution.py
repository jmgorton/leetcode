from typing import List
from math import inf

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # ans = -1
        ### Trie approach 
        trie = {} # keys as nested trie, possible targets and costs as dict at key `None` ?? 
        for orig, chg, c in zip(original, changed, cost):
            fromNode = trie
            for fr in orig:
                if fr not in fromNode: fromNode[fr] = {}
                fromNode = fromNode[fr]
            if None not in fromNode: fromNode[None] = {}
            if chg not in fromNode[None]: fromNode[None][chg] = c
            else: 
                fromNode[None][chg] = min(fromNode[None][chg], c)
            # if chg also exists in our trie, we have to try to include that 
            # in the trie result for orig with the new cost and target
            # e.g. if here we have a way to update ab -> cd, and cd exists in the trie,
            # such that we can update cd -> ef, we now have a way to update ab -> ef
            toNode = trie
            for to in chg:
                if to not in toNode:
                    toNode = { None: {} } # None
                    break
                toNode = toNode[to]
            # for k, v in toNode[None].items():
            #     if k in fromNode: fromNode[k] = min(fromNode[k], v)
            #     else: fromNode[k] = v
            #     # fromNode[None][k] = min(fromNode[None][k] or inf, v)
            # for k, v in fromNode[None].items():
            #     if k in toNode: toNode[k] = min(toNode[k], v)
            #     else: toNode[k] = v
        print(trie)
        best = [0] + [inf] * len(source) # [0] ?? 
        # for i, v in enumerate(source):
        for i in range(len(source)):
            node = trie
            j = i
            while j < len(source) and source[j] in node:
                node = node[source[j]]
                j += 1
                if None in node and target[i:j] in node[None]:
                    best[j] = min(best[j], best[i] + node[None][target[i:j]])
        # return ans
        if best[-1] < inf: return best
        return -1
    

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
    },
    {
        "in": ("abcdefgh", "acdeeghh", ["bcd","fgh","thh"], ["cde","thh","ghh"], [1,3,5]),
        "out": 9
    },
    {
        "in": ("abcdefgh", "addddddd", ["bcd","defgh"], ["ddd","ddddd"], [100,1578]),
        "out": -1
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        result = sol.minimumCost(*test["in"])
        assert test["out"] == result, f"Expected {test["out"]}, got {result}"
    print(f"All tests passed.")