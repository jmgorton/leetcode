from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        ### tbh, way overthinking this 
        # can just sum rows and check cols as we go,
        # slight speedup to store notSpecialCols

        notSpecial = set()
        result = 0
        for i, row in enumerate(mat):
            if sum(row) != 1: continue
            col = row.index(1)
            if col in notSpecial: continue
            # if any(mat[i][col] for i in range(len(mat)) if mat[i] != row):
            if any(mat[j][col] for j in range(i) + range(i+1, len(mat))):
                notSpecial.add(col)
            else: result += 1
        return result

        # maybeSpecial = {}
        # for row in mat:
        #     if sum(row) == 1:
        #         maybeSpecial[row.index(1)] = maybeSpecial.get(row.index(1), 0) + 1
            
        # count = 0
        # for v in maybeSpecial.values():
        #     if v == 1:
        #         count += 1
        # return count

        # maybeSpecialCol = set()
        # notSpecialCol = set()
        # for row in mat:
        #     maybeSpecialRow = None
        #     for i, v in enumerate(row):
        #         if not v: continue
        #         if maybeSpecialRow == False:
        #             notSpecialCol.add(i) 
        #         elif maybeSpecialRow == True:
        #             maybeSpecialRow = False
        #             notSpecialCol |= maybeSpecialCol | {i}
        #         else: # if maybeSpecialRow == None:
        #             # maybeSpecialRow = True
        #             # maybeSpecialCol.add(i)
        #             if i in maybeSpecialCol or i in notSpecialCol:
        #                 notSpecialCol.add(i)
        #                 maybeSpecialCol.discard(i)

            
        # # count = 0
        # # for v in maybeSpecial.values():
        # #     if v == 1:
        # #         count += 1
        # # return count