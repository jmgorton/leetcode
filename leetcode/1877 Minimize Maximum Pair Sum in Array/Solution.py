from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(map(lambda x: x[0] + x[1], zip(nums[:len(nums)//2], reversed(nums[len(nums)//2:]))))

# LMAO, one of the top solutions just put this line at the end of their very normal solution
# __import__("atexit").register(lambda: open("display_runtime.txt","w").write("000"))

tests = [
    {
        "in": [3,5,2,3],
        "out": 7
    },
    {
        "in": [3,5,4,2,4,6],
        "out": 8
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        if (act := sol.minPairSum(test["in"])) != test["out"]:
            print(f"Expected {test["out"]}; Got {act}")
