class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0 
        isZero = True
        for c in s:
            if (c == '0') ^ isZero: ans += 1
            isZero = not isZero
        return min(ans, len(s) - ans)