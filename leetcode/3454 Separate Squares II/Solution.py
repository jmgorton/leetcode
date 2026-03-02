from heapq import *
from bisect import *
from typing import List
# import SegmentTree
# from SegmentTree import SegmentTree

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Yesterday's Example 2 (see: 3453):
        # At y=0: A=0
        # At y=1: A=2
        # At y=2: A=5
        # Split happens at 2.5 per side
        # Starting at y=1 and going to y=2...
        #   gain 3sq per 1y traveled 
        #   want to gain 0.5sq
        #   travel 0.5/3 above y=1
        # Result: y=1.16667 (y=7/6) 

        # Today, overlaps are only counted once
        # we're gonna have to combine the heap approach 
        # with some sort of union-find type of approach maybe 

        # alternatively, we could adapt the same approach as yesterday
        # and just add negative square(s) as necessary to cancel out any 
        # locations that may overlap... seems more difficult than first idea

        # the union find has to keep track of bands of x-coords
        # that are currently covered, and it has to also track
        # depth of the band, so when one square ends, we know if 
        # it is covered by other squares, or if it exposes uncovered area

        # we can have a list of critical x-coords that indicates gain/loss
        # of depth (or maybe it stays the same), when a square ends, we can 
        # decrement all critical points in the range [x_i, x_i + l_i] 
        # and look for bands of that updated range that fell to 0

        # we'll want the critical x-coords list to be sorted, and we'll have
        # to be able to insert/delete/update from any index within that list 
        # probably meaning it'll be necessary to do some sort of bisect search
        # it could be worthwhile to make a data structure that combines 
        # array-style index lookups (for bisect) with linked-list-style inserts
        # i guess that's only possible (feasible) if we have a linked list
        # contained at every array index, and aim for every linked list to have 
        # a length of 1; every now and then we flatten the linked list and 
        # re-index the array if one of the lists gets too long (i.e. tons of inserts
        # happened without yet seeing a delete... but then the deletes will come and
        # our array will have a bunch of null elements or references to the same element)
        # let's not bother with all that, just use an array for now i suppose 
        # maybe combine it with a map or something ... i'm going for a walk 
        # aha! we don't need to insert! we can make sure every critical point already exists
        # in the array during the initial traversal, we could even make a map for O(1) lookup
        # let's make the vertical edges a map with the current x_i coord, the depth
        # of the overlap at that x_i, and maybe a couple refs... to the x_j of the next
        # critical x-coord and the x_k of the next d=0/d>=1 toggle maybe 

        horizontalEdges = [] # (y_i, l_i)
        # verticalEdges = {} # [] # (x_i, d) ... {x_h, x_j, x_k}
        # # keys in verticalEdges are the x-coords
        # # values in verticalEdges are (depth, prev critical x-coord, next critical x-coord, next step change)
        # # where step change is the transition between the two steps: d=0 or d>=1
        # verticalEdges[0] = [0, None, 10 ** 9, None]
        # verticalEdges[10 ** 9] = [0, 0, None, None]

        # meh, trash all that, verticalEdges is an array with (x_i, d) 
        # we'll sort it after building it and then just bisect and iterate
        verticalEdges = set() # []
        # but this time, we can't pre-compute totalArea very easily ...
        # we could store the running total for area in a separate array
        # and find the halfway point at the end i guess 

        for (xi, yi, li) in squares: # O(n)
            # verticalEdges[xi]
            # verticalEdges.append((xi, 0))
            # verticalEdges.append((xi + li, 0)) # not checking for duplicates
            verticalEdges.add(xi)
            verticalEdges.add(xi + li) # ok, don't allow duplicates
            heappush(horizontalEdges, (yi, xi, li)) # O(n log n)
            heappush(horizontalEdges, (yi + li, xi, -li)) # O(n log n)
        
        # verticalEdges.sort(key=lambda xi: xi[0])
        # verticalEdges = map(lambda item: (item, 0), sorted(verticalEdges))
        verticalEdges = sorted(list(map(lambda item: [item, 0], verticalEdges))) # O(n log n)
        # reassign vertical edges from a Set to a sorted List 

        velocity = posY = 0 # runningTotalArea = 0
        areaUnderAtPosY = [(0, 0)] # area, posY

        while horizontalEdges: # O(n)
            (nextY, someX, someL) = heappop(horizontalEdges) # O(log n) inside O(n) 
            diffY = nextY - posY
            areaUnderAtPosY.append((areaUnderAtPosY[-1][0] + (diffY * velocity), nextY))
            posY = nextY
            diffD = 1 if someL > 0 else -1
            critDAtX = 0 if someL > 0 else 1
            # someX and someX + |someL| both guaranteed to exist in list
            ivx = bisect_left(verticalEdges, [someX, -1]) # O(log n) inside O(n) 
            # (xiv, d) = verticalEdges[ivx]
            # ivx += 1
            # while (verticalEdges[ivx][0] <= someX + someL):
            while True: # O(n) ?? inside O(n) ... 
                # if (ivx == len(verticalEdges) or verticalEdges[ivx][0] > someX + someL): break
                if (verticalEdges[ivx][0] == someX + (someL * diffD)): break
                xiv, d = verticalEdges[ivx]
                if (d == critDAtX):
                    velocity += diffD * (verticalEdges[ivx + 1][0] - xiv)
                verticalEdges[ivx][1] += diffD
                ivx += 1
        
        totalCoveredArea = areaUnderAtPosY[-1][0]
        targetCoveredAreaSplit = totalCoveredArea / 2
        iau = bisect_left(areaUnderAtPosY, (targetCoveredAreaSplit, -1)) # O(log n)
        areaLowerB, posYLowerB = areaUnderAtPosY[iau - 1]
        areaUpperB, posYUpperB = areaUnderAtPosY[iau]

        frac = (targetCoveredAreaSplit - areaLowerB) / (areaUpperB - areaLowerB)
        partialY = (posYUpperB - posYLowerB) * frac
        
        return posYLowerB + partialY
    

# time limit exceeded on TestCase1 (695/753)
# seems like my runtime complexity should be maybe O(n log n)?? or maybe O(n ** 2)... 
# idk, but we probably need to figure out a better way to handle the critical x-coords 
# to get rid of that while block updating x-coord depths inside the while heap popper 
