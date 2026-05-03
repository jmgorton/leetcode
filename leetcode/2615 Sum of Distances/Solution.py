from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # lookup = {}
        # for i, v in enumerate(nums):
        #     if v not in lookup: lookup[v] = [0, 0] 
        #     lookup[v][0] += 1
        #     lookup[v][1] += i
        
        # result = []
        # for i, v in enumerate(nums):
        #     result.append(abs(lookup[v][0] * i - lookup[v][1]))
        # # # WRONG 

        # actually, store the distance between each instance of v
        # the pattern is ... pascal? no
        # consider value v at index i1, a gap of g1, v at i2, a gap of g2
        # and a final value of v at index i3, so 3 instances and 2 gaps 
        # for the first instance, the result is 2*g1 + 1*g2
        # for the second instance, 1*g1 + 1*g2
        # and for the third, 1*g1 + 2*g2
        # the coefficient counts up from the ends towards the value 
        # in this case it's symmetric, doesn't have to be 

        lookup = {}
        for i, v in enumerate(nums):
            # if v in lookup: lookup[v].append(i - lookup[v][-1])
            # else: lookup[v] = [i]
            if v not in lookup: lookup[v] = []
            lookup[v].append(i)
        
        result = []
        for i, v in enumerate(nums):
            if len(lookup[v]) == 1:
                result.append(0)
                continue
            # for a, b in pairwise(lookup)
            partial = 0
            # if lookup[v][0] != i:
            #     j = 1
            #     while lookup[v][j] != i:
            #         partial += j * (lookup[v][j] - lookup[v][j - 1])
            #         j += 1
            j = 0
            while lookup[v][j] != i:
                partial += (j + 1) * (lookup[v][j + 1] - lookup[v][j])
                j += 1
                
            # if lookup[v][-1] != i:
            #     j = -1
            #     while lookup[v][j - 1] != i:
            #         partial -= j * (lookup[v][j] - lookup[v][j - 1])
            #         j -= 1
            j = -1
            while lookup[v][j] != i:
                partial -= j * (lookup[v][j] - lookup[v][j - 1])
                j -= 1
            result.append(partial) 
        return result 
        
        # # # TLE
        # we're getting closer... we can speed up the gap multiplication 
        # computation some i bet, there might even be a nice way to 
        # simplify it way down into something really efficient, idk 
