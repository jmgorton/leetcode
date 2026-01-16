from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        # how to construct possible square side lengths
        # we are focused on the gaps between fences and making contiguous configs 
        # at each fence processed in order, we have a certain number of configurations 
        # we could have achieved by the time we got here, and they can be grouped into 
        # two groups: previously ended, or ongoing. At each fence, from the ongoing, we
        # can either end it here, or we can keep going. Additionally, we can start a new
        # configuration at this fence. 

        hFences.sort()
        vFences.sort()
        hSideLengths = set()
        hSideLengthsFinal = set()
        prevH = 1
        for h in hFences + [m]:
            hl = h - prevH
            hSideLengthsFinal |= hSideLengths
            hSideLengths = {x + hl for x in hSideLengths}
            hSideLengths.add(hl) 
            prevH = h
        hSideLengthsFinal |= hSideLengths
        vSideLengths = set()
        vSideLengthsFinal = set()
        prevV = 1
        for v in vFences + [n]:
            vl = v - prevV
            vSideLengthsFinal |= vSideLengths
            vSideLengths = {x + vl for x in vSideLengths}
            vSideLengths.add(vl) 
            prevV = v
        vSideLengthsFinal |= vSideLengths
        possibleSquares = vSideLengthsFinal & hSideLengthsFinal
        if not possibleSquares: return -1
        return (max(possibleSquares) ** 2) % (10 ** 9 + 7)