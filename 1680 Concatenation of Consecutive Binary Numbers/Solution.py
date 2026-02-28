class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Python solution
        return int("".join([f"{x:b}" for x in range(1, n + 1)]), 2) % (10 ** 9 + 7)