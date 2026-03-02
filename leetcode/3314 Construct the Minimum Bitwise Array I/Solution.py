from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        # The bitwise OR of a number n with it's nearest incremented neighbor n+1
        # 

        # 2 is the only weird case
        #   - the only even prime, i.e. the only possible input with a 0 in the binary 1's digit 
        #   - the only (??) element of ans that has to be negative... because it's impossible
        #     - it is impossible to find an n such that n | n+1 == 2

        # essentially, the LSB, n_lsb0, of n that is a 0 will get flipped to a 1 in n+1
        # all bits less significant than n_lsb0 will in turn be flipped to 0
        # and the bitwise or of n 

        # so, given some number n, to find the value of the bitwise OR of n | n+1,
        # you find the first 0 bit (from least-significant to most-) and just flip
        # it to a 1... therefore, the bitwise OR of n | n+1 will have exactly 1 more 
        # bit "on" than n did. therefore, the only number that can possibly have
        # exactly 1 bit flipped on after this operation would be 0

        # and to get the original n, we can trivially flip the lsb we find that's a 1,
        # for an input prime p in nums, p-1 always satisfies the condition (for p>2)
        # but to minimize the result, we have to follow the full chain of leading,
        # or least-significant, 1 bits and flip the *last* one we find before we encounter
        # *any* 0 bits. 


        # 2: 10 -> NOT POSSIBLE
        # 3: 11 -> 1 (10) 
        # 5: 101 -> 100 (101) 
        # 7: 111 -> 11 (100) 
        # 11: 1011 -> 1001 (1010)
        # 13: 1101 -> 1100 (1101)
        # 17: 10001 -> 10000 (10001)
        # 19: 10011 -> 10001 (10010) 

        # 31: 11111 -> 1111 (10000) 

        ans = []
        for num in nums:
            mask = 0b1
            if not (num & mask): ans.append(-1); continue
            while (num & mask): mask <<= 1
            mask >>= 1
            ans.append(num ^ mask)
        return ans
