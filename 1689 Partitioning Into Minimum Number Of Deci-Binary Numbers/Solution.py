from collections import Counter

class Solution:
    def minPartitions(self, n: str) -> int:
        # return max([int(c) for c in n])
        return max([int(k) for k in Counter(n).keys()])