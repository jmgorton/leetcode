class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n:
            if not bool(n & 1) ^ n & bool(n & 2): return False
            n >>= 1
        return True