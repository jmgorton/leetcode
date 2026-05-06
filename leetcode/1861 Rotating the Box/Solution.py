from typing import List
from itertools import groupby

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        result = []
        for row in boxGrid:
            result.append([])
            for k, g in groupby(row, key=lambda x: x == '*'):
                if k: result[-1].extend(g)
                else:
                    stones = blanks = 0
                    for item in g:
                        if item == '#': stones += 1
                        else: blanks += 1
                    result[-1].extend(['.'] * blanks)
                    result[-1].extend(['#'] * stones)
        return [x[::-1] for x in zip(*result)]