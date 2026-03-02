from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        # Same problem as yesterday (3314) but with larger possible input values in nums 
        # In the community solutions, there was a clever O(1) method for finding 
        # ans[i] given an input value nums[i] ... involving bitwise ops on the negative ...
        # or the 1's complement, or something ... of nums[i]... 
        # here's the O(1) way to find the solution, i checked:
        # if num % 2: ans[i] = (num - ((num + 1) & (-num - 1)) // 2)
        # for some reason, my solution (below, same as yesterday) beat 100% at 0ms this time
        # on yesterday's problem (easier) it took 4ms, oh well, that's Python for ya 
        # how does that work??? 
        # looks like the basic idea that python's bitwise & between x & -x 
        # for some reason only matches the first 1 & 1 bits and then truncates...
        # perhaps due to the fact that python numbers use arbitrary precision, and 
        # negative numbers are treated as having infinite leading 1's ... but 
        # it's not smart enough to see that the positive number doesn't??? 
        # whoever came up with that solution must be a genius or something 

        ans = []
        for num in nums:
            mask = 0b1
            if not (num & mask): ans.append(-1); continue
            while (num & mask): mask <<= 1
            mask >>= 1
            ans.append(num ^ mask)
        for i in range(len(nums)): print(f"{nums[i]:b} => {ans[i]:b} ... {(nums[i] + 1):b} ({nums[i] + 1}) & {(-nums[i] - 1):b} ({-nums[i] - 1}) = {((nums[i] + 1) & (-nums[i] - 1)):b} ({((nums[i] + 1) & (-nums[i] - 1))}) // 2 = {(((nums[i] + 1) & (-nums[i] - 1)) // 2)} ... {(nums[i] - ((nums[i] + 1) & (-nums[i] - 1)) // 2):b}") 
        # {-i:b} just negative ... ({~-i:b}) just i-1 ... i:{nums[i]:b} the input ... 1's complement ~i:{~nums[i]:b}
        return ans

if __name__ == "__main__":
    sol = Solution()
    sol.minBitwiseArray([2,3,5,7,11,13,17,19,31,101])


