from itertools import groupby

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(list(groupby(s))) <= 2