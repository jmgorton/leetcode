class Solution:
    def mirrorDistance(self, n: int) -> int:
        # def reverse(n: int) -> int:
        #     if not n: return 0
        #     o = 1
        #     while n:
        #         n, c = divmod(n, 10)
        return abs(n - int(f"{n}"[::-1]))