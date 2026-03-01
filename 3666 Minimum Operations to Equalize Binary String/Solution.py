

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # zeroes = s.count('0')
        ones = s.count('1')
        n = len(s) 
        if ones == n: return 0

        allZeroes = True # ones == 0
        result = 0
        # while zeroes != 0: # ones != n...
        while ones != 0 or allZeroes:
            # print(zeroes) 
            # zeroes = (zeroes - k) % n
            # print(zeroes) 
            print(ones)
            ones += k
            if ones >= n: allZeroes = not allZeroes
            ones %= n
            print(ones)
            result += 1
            if result == n: break # allOnes ... allZeroes
        return result if result < n else -1 