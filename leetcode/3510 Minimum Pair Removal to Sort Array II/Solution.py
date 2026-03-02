from typing import List 
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # print(nums)
        # handle the operations according to problem's criteria 
        heap = []
        # essentially making a linked list underlying the list here 
        next = {x: x+1 for x in range(len(nums))}
        prev = {x: x-1 for x in range(len(nums))}
        next[len(nums)-1] = None
        prev[0] = None
        # the indices in the linked list version of the list that are followed by a lower number
        decr = set()
        for i, v in enumerate(nums[:-1]):
            heapq.heappush(heap, (v + nums[i+1], i))
            if nums[i+1] < v: decr.add(i)
        # print(decr)
        ans = 0
        while decr and heap:
            (newVal, iToUpdate) = heapq.heappop(heap)
            iToDelete = next[iToUpdate] # valid elements to update will always have an element to delete that follows them 
            if not iToDelete: 
                # print(f"Skipping op on nums[{iToUpdate}]={nums[iToUpdate]} due to no element following")
                continue # iToUpdate was already updated previously, this is a leftover heap item 
            if newVal != nums[iToUpdate] + nums[iToDelete]: 
                # print(f"Skipping op on nums[{iToUpdate}]={nums[iToUpdate]} due to outdated heap item (expected {newVal}, nums[{iToDelete}]={nums[iToDelete]})")
                continue # already updated, skip this item 
            # out = f"({nums[iToUpdate]} + {nums[iToDelete]} = {newVal}) -> "
            ans += 1
            nums[iToUpdate] = newVal
            # update iToUpdate & iPrev 
            iPrev = prev[iToUpdate] 
            if iPrev != None: 
                # next[iPrev] = iToUpdate
                if nums[iPrev] > newVal: decr.add(iPrev)
                else: decr.discard(iPrev)
                heapq.heappush(heap, (nums[iPrev] + newVal, iPrev))
            # update iToUpdate & iNext and delete iToDelete
            iNext = next[iToDelete]
            prev[iToDelete] = next[iToDelete] = None
            decr.discard(iToDelete)
            next[iToUpdate] = iNext
            if iNext: 
                prev[iNext] = iToUpdate
                if nums[iNext] < newVal: decr.add(iToUpdate)
                else: decr.discard(iToUpdate)
                heapq.heappush(heap, (newVal + nums[iNext], iToUpdate))
            # elif len(decr) == 1:
            #     for el in decr: 
            #         if el == iToUpdate: return ans
            else: decr.discard(iToUpdate)
            # if next[iToDelete] and newVal <= nums[next[iToDelete]]: decr.discard(iToDelete) # this is close, and seems important...

            # # print debugging
            out = ""
            for i in range(len(nums)):
                if next[i]:
                    out += "["
                    out += str(nums[i])
                    ix = next[i]
                    while ix:
                        out += ", "
                        out += str(nums[ix])
                        ix = next[ix]
                    out += "]"
                    out += f" <- ({nums[iToUpdate]} + {nums[iToDelete]} = {newVal})"
                    break
            if not out:
                print(decr, heap)
            print(out)
        
        # print(decr)
        # print(heap)
            
        return ans


testCases = [
    {
        "in": [5,2,3,1],
        "out": 2
    },
    {
        "in": [1,2,2],
        "out": 0
    },
    {
        "in": [5],
        "out": 0
    },
    {
        "in": [2,2,-1,3,-2,2,1,1,1,0,-1],
        # [2,2,-1,3,0,1,1,1,0,-1] 1
        # [2,2,-1,3,0,1,1,1,-1] 2
        # [2,2,-1,3,0,1,1,0] 3
        # [2,1,3,0,1,1,0] 4 ... ah, shoot, i was wrong 
        # [2,1,3,1,1,0] 5
        # [2,1,3,1,1] 6
        # [2,1,3,2] 7
        # [3,3,2] 8
        # [3,5] 9
        "out": 9
    },
    {
        "in": [-2,1,2,-1,-1,-2,-2,-1,-1,1,1],
        # [-2,1,2,-1,-1,-4,-1,-1,1,1] 1
        # [-2,1,2,-1,-5,-1,-1,1,1] 2
        # [-2,1,2,-6,-1,-1,1,1] 3
        # [-2,1,2,-7,-1,1,1] 4
        # [-2,1,2,-8,1,1] 5
        "out": 10
    },
    {
        "in": [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-280,168,-32,-547,-310,-719,629,-600,165,613,-302,-720,-208,-249,188,75],
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-280,168,-32,-547,-1029,629,-600,165,613,-302,-720,-208,-249,188,75] (-310+-719) 1
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-280,168,-32,-1576,629,-600,165,613,-302,-720,-208,-249,188,75] (-547+-1029) 2
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-280,168,-1608,629,-600,165,613,-302,-720,-208,-249,188,75] (-32+-1576) 3
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-280,-1440,629,-600,165,613,-302,-720,-208,-249,188,75] (168,-1608) 4
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-272,-1720,629,-600,165,613,-302,-720,-208,-249,188,75] (-280,-1440) 5
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,602,-1992,629,-600,165,613,-302,-720,-208,-249,188,75] (-272,-1720) 6
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-302,-720,-208,-249,188,75] (602,-1992) 7
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1022,-208,-249,188,75] (-302,-720) 8 **
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1230,-249,188,75] (-1022,-208) 9
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1479,188,75] (-1230,-249) 10
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1291,75] (-1479,188) 11
        # [-746,-125,-343,-586,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1291,75) 12
        # [-746,-125,-929,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-343,-586) 13 **
        # [-746,-1054,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-125,-929) 14
        # [-1800,90,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-746,-1054) 15
        # [-1710,404,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1800,90) 16
        # [-1306,-285,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1710,404) 17
        # [-1591,136,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1306,-285) 18
        # [-1455,-479,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1591,136) 19
        # [-1934,159,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1455,-479) 20
        # [-1775,683,519,-115,533,-1390,629,-600,165,613,-1216] (-1934,159) 21
        # [-1092,519,-115,533,-1390,629,-600,165,613,-1216] (-1775,683) 22
        # [-1092,519,-115,-857,629,-600,165,613,-1216] (533,-1390) 23 ** 
        # [-1092,519,-972,629,-600,165,613,-1216] (-115,-857) 24
        # [-1092,519,-972,629,-600,165,-603] (613,-1216) 25 **
        # [-573,-972,629,-600,165,-603] (-1092,519) 26 **
        # [-1545,629,-600,165,-603] (-573,-972) 27
        # [-916,-600,165,-603] (-1545,629) 28
        # [-1516,165,-603] (-916,-600) 29
        # [-1351,-603] (-1516,165) 30
        "out": 30
    }
]
            
if __name__ == "__main__":
    sol = Solution()
    for test in testCases[5:]:
        if (act := sol.minimumPairRemoval(test["in"])) != test["out"]:
            print(f"Expected {test['out']}; Got {act}")
        else: print("Success")