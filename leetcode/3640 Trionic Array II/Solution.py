from typing import List
from math import inf

### Solution

# the main trick with this one is that the elements of nums can be negative, and 
# if that's the case, we can terminate the increasing sections of the 
# trionic array early (or begin late) ... we just need to make sure 
# the strictly decreasing portion of the trionic array is wrapped by 
# at least one increasing contiguous pair of elements on either side
# 
# since the decreasing section of the array is wrapped by increasing sections
# of the array, we just need to:
# 1. for the close/post wrapper, include only a single element following, UNLESS
#   the overall value of the increasing segment becomes positive 
# 2. for the open/pre wrapper, include all of the positive elements leading up 
#   to the first peak, OR just a single negative element 

# the other trick is that the structure of this array is not guaranteed, and 
# our job isn't just to determine whether it *is* a trionic array; we have to 
# identify subarrays that are trionic. for that we have to identify contiguous 
# sections of alternating monotonically increasing/decreasing subarrays, 
# starting with increasing. One point to make: if we find a peak, the only way 
# this peak does not correspond to *some* trionic array is if there is a sequence
# of two identical numbers in a row in the array. We can start our algorithm
# by looking for peaks, and tracking where the monotonically increasing portion
# of the ascent crossed 0, which is where our ideal trionic array starts (as well
# as the running sum from that point). When we find a peak, we continue summing 
# down the descent, looking for either a plateau (discard the peak we found), or 
# a trough. Two things must be done on the ascent following this trough: 
# 1. we return to step 1 and start looking for another peak, storing the relevant
#   information and considering it the potential start of a new trionic subarray,
# 2. and simultaneously, we track the entire sum of the following ascent to see
#   if it becomes positive 

class Solution:
    def maxSumTrionic(self, nums: List[int], debug: bool = False) -> int:
        # best = -inf
        # firstAscPosSum = 0
        # secondAscTotalSum = 0
        # secondAscPosSum = 0
        # secondAscFirstEl = None
        # descTotalSum = 0
        # wasAscending = False
        # wasDescending = False
        # i = 1
        # while i < len(nums):
        #     if nums[i] == nums[i - 1]: # invalid, set best and clear data
        #         if wasAscending and wasDescending:
        #             best = max(best, firstAscPosSum + descTotalSum + (secondAscTotalSum if secondAscTotalSum > 0 else secondAscFirstEl))
        #         firstAscPosSum = secondAscTotalSum = descTotalSum = 0
        #         secondAscFirstEl = None
        #         wasAscending = wasDescending = False
        #     elif nums[i] > nums[i - 1]: # ascending
        #         wasAscending = True
        #         if wasDescending and secondAscFirstEl == None: secondAscFirstEl = nums[i]
        #         if nums[i - 1] > 0: 
        #             firstAscPosSum += nums[i - 1]
        #             secondAscPosSum += nums[i - 1]
        #         if wasDescending: 
        #             secondAscTotalSum += nums[i - 1]
        #     elif nums[i] < nums[i - 1]: # descending
        #         wasDescending = wasAscending
        #         if secondAscFirstEl != None: # the end of the second ascent 
        #             best = max(best, firstAscPosSum + descTotalSum + (secondAscTotalSum if secondAscTotalSum > 0 else secondAscFirstEl))
        #             firstAscPosSum = secondAscPosSum 
                    
        #         if wasAscending: 
        #             descTotalSum += nums[i - 1]
        #             if firstAscPosSum <= 0: firstAscPosSum = nums[i - 2]

        # return 

        ### new approach 

        peakIndex = troughIndex = None
        ascPosSum = ascTotSum = mtnSum = 0
        best = -inf
        i = 1
        while i < len(nums):
            if nums[i] <= nums[i - 1]: # valid descents are handling inside the ascent peak logic, here it's invalid 
                # but this could be the end of a previous valid trionic array
                if peakIndex and troughIndex:
                    if debug: print(f"Found trionic: peak={peakIndex}; trough={troughIndex}; mtnSum={mtnSum}; ascTotSum={ascTotSum}")
                    # if ascTotSum - nums[troughIndex] > nums[troughIndex + 1]: best = max(best, mtnSum + ascTotSum - nums[troughIndex]) # both ascTotSum and mtnSum include trough 
                    # else: best = max(best, mtnSum + nums[troughIndex + 1])
                    best = max(best, mtnSum + max(nums[troughIndex + 1], ascTotSum - nums[troughIndex]))
                    if debug: print(f"New best: {best}")
                peakIndex = troughIndex = None
                ascPosSum = ascTotSum = mtnSum = 0
                i += 1
                continue
            # otherwise we're ascending, either first or second peak (or one of each in different trionic subarrays) 
            if i == len(nums) - 1 or nums[i] > nums[i + 1]: # found peak at i, handle descent and jump i forward 
                if peakIndex and troughIndex:
                    if debug: print(f"Found trionic: peak={peakIndex}; trough={troughIndex}; mtnSum={mtnSum}; ascTotSum={ascTotSum}")
                    if (ascTotSum - nums[troughIndex] + nums[i]) > nums[troughIndex + 1]: best = max(best, mtnSum + ascTotSum - nums[troughIndex] + nums[i]) # both ascTotSum and mtnSum include trough 
                    else: best = max(best, mtnSum + nums[troughIndex + 1])
                    if debug: print(f"New best: {best}")
                peakIndex = i
                j = i + 1
                if ascPosSum: mtnSum = ascPosSum + nums[i]
                else: mtnSum = nums[i - 1] + nums[i]
                while j < len(nums) and nums[j] < nums[j - 1]:
                    mtnSum += nums[j]
                    j += 1
                if j == len(nums): break # not trionic
                if nums[j] == nums[j - 1]: # not trionic
                    i = j
                    peakIndex = troughIndex = None
                    ascPosSum = ascTotSum = mtnSum = 0
                else: # found trough at j - 1, this is a valid trionic subarray 
                    troughIndex = j - 1
                    i = j
                    ascTotSum = nums[j - 1] # + nums[j]
                    if nums[j - 1] > 0: ascPosSum = nums[j - 1]
                    continue
            ascTotSum += nums[i]
            if nums[i] > 0: ascPosSum += nums[i]
            i += 1
        return best

tests = [
    {
        "in": (([0,-2,-1,-3,0,2,-1], False)),
        "out": -4
    },
    {
        "in": (([1,4,2,7], False)),
        "out": 14
    },
    {
        "in": (([159,208,-920,-460,295], False)),
        "out": -718
    },
    {
        "in": ([126,200,-584,370,520,-682,450,-136,448], True),
        "out": 658
    }
]

if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        actual = sol.maxSumTrionic(*test["in"])
        assert actual == test["out"], f"Expected {test["out"]}, got {actual}"
    print("All tests passed")