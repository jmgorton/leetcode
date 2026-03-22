from itertools import chain
from typing import List

class Solution:
    def findRotation(self, I: List[List[int]], R: List[List[int]]) -> bool:
        if all(x == y for x, y in zip(chain(*I), chain(*R))): return True
        if all(x == y for x, y in zip(chain([x for row in I[::-1] for x in row[::-1]]), chain(*R))): return True
        # T = zip(*I) # this is a transposition, not a rotation
        I90 = chain(*zip(*I[::-1])) # this is a rotation 
        if all(x == y for x, y in zip(chain(*zip(*I[::-1])), chain(*R))): return True
        # if all(x == y for x, y in zip(chain([x for row in zip(*I[::-1]) for x in row[::-1]]), chain(*R))): return True
        if all(x == y for x, y in zip(chain(*zip(*R[::-1])), chain(*I))): return True
        return False
