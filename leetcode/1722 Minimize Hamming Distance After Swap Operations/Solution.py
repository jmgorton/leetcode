from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        lookup = {0: {i for i in range(n)}} # dict 
        keyRef = [0] * n # array 
        removedKeys = [] # heap 

        # union find 
        for a, b in allowedSwaps:
            aSet = {a} if not keyRef[a] else lookup[keyRef[a]] 
            bSet = {b} if not keyRef[b] else lookup[keyRef[b]]
            
            if bool(keyRef[a]) ^ bool(keyRef[b]):
                if keyRef[a]:
                    keyRef[b] = keyRef[a]
                    lookup[0].discard(b)
                    lookup[keyRef[a]].add(b)
                else:
                    keyRef[a] = keyRef[b]
                    lookup[0].discard(a)
                    lookup[keyRef[b]].add(a)
            else:
                if keyRef[a] and keyRef[b]:
                    if keyRef[a] in lookup: del lookup[keyRef[a]]
                    if keyRef[b] in lookup: del lookup[keyRef[b]]
                    heappush(removedKeys, keyRef[a])
                    heappush(removedKeys, keyRef[b])
                else:
                    lookup[0].discard(a)
                    lookup[0].discard(b)
                newKey = heappop(removedKeys) if removedKeys else len(lookup)
                lookup[newKey] = aSet | bSet 
                for x in lookup[newKey]:
                    keyRef[x] = newKey

        result = 0 
        # based on unions, compare source to target
        for k, s in lookup.items():
            if k:
                src = {}
                trg = {}
                for e in s:
                    src[source[e]] = 1 if source[e] not in src else (src[source[e]] + 1)
                    trg[target[e]] = 1 if target[e] not in trg else (trg[target[e]] + 1)
                dupes = 0
                for v, c in src.items():
                    if v in trg: dupes += min(c, trg[v])
                result += len(s) - dupes
            else:
                for e in s:
                    if source[e] != target[e]: result += 1
        return result 
