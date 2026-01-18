from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        # at least naively... we can:

        # need to check the vertical columns, horizontal row, and both diagonals...
        # calculate memos for horizontal, vertical, and tl-br diagonals
        # turn grid[x][y] into targets[x][y][size] where size <= min(x,y) 
        # targets[x][y][size] returns how much each row/col/diag would have to 
        # sum to if a magic square of size existed with bottom right corner (x,y)

        # (could even store a small dict or list at targets[x][y][size] with the keys:
        # horiz, vert, diag...) 

        # then, for each square in grid, consider it the bottom right corner
        # of a potential magic square, get the set of potential sizes that 
        # magic square might be by checking 
        #   - that horiz, vert, and diag at [x][y] are equal
        #   - that horiz from targets[x][y-size+1...y][size] are equal
        #   - that vert from targets[x-size+1...x][y][size] are equal 

        # for these potential sizes that satisfy horiz, vert, and tl-br diag
        # conditionals, only other filter to apply is the bl-tr diag ...

        # get the max of those that satisfy all four 

        # i can't think of any more clever way to solve it 
        # but i can imagine there could be a speed up when checking neighbors, idk

        VERT = 0
        HORIZ = 1
        TLBRDIAG = 2
        BLTRDIAG = 3

        # assumes relevant targetSums info is already built/computed 
        def isBottomRightCornerOfMagicSquareOfSize(ix: int, iy: int, isz: int) -> bool: # consider isz==0 to be a single square 
            # print(f"Checking grid[{iy}][{ix}] with isz={isz}...")
            if not all(map(lambda x: x == targetSums[iy][ix][isz][0], targetSums[iy][ix][isz][:BLTRDIAG])): return False
            if not all(map(lambda x: x == targetSums[iy][ix][isz][0], [targetSums[iy-isx][ix][isz][HORIZ] for isx in range(1, isz+1)])): return False
            if not all(map(lambda x: x == targetSums[iy][ix][isz][0], [targetSums[iy][ix-isy][isz][VERT] for isy in range(1, isz+1)])): return False
            return targetSums[iy][ix - isz][isz][BLTRDIAG] == targetSums[iy][ix][isz][0] 

        targetSums = [[[[x] * 4] for x in row] for row in grid] 
        # targetSums = [[[x] * 4 for x in row] for row in grid] # ... how does that execute? i use 4 bracket indices...
        # print(targetSums)
        largestMagicSquare = 1
        for iy in range(len(grid)):
            for ix in range(len(grid[iy])):
                maxSquareSize = min(ix, iy) # maxSquareSize of 0 == individual square
                bltrMaxSquareSize = min(iy, len(grid[0]) - 1 - ix)
                for isz in range(1, max(ix, iy, maxSquareSize, bltrMaxSquareSize) + 1):
                    targetsBySizeHere = [-1, -1, -1, -1]
                    if isz <= ix: targetsBySizeHere[HORIZ] = targetSums[iy][ix - 1][isz - 1][HORIZ] + grid[iy][ix]
                    if isz <= iy: targetsBySizeHere[VERT] = prev + grid[iy][ix] if (prev := targetSums[iy - 1][ix][isz - 1][VERT]) > -1 else grid[iy][ix]
                    if isz <= maxSquareSize: targetsBySizeHere[TLBRDIAG] = prev + grid[iy][ix] if (prev := targetSums[iy - 1][ix - 1][isz - 1][TLBRDIAG]) > -1 else grid[iy][ix]
                    if isz <= bltrMaxSquareSize: targetsBySizeHere[BLTRDIAG] =  prev + grid[iy][ix] if (prev := targetSums[iy - 1][ix + 1][isz - 1][BLTRDIAG]) > -1 else grid[iy][ix]
                    # print(f"Before: {targetSums[iy][ix]}")
                    targetSums[iy][ix].append(targetsBySizeHere)
                    # print(f"After: {targetSums[iy][ix]}")
                    if isBottomRightCornerOfMagicSquareOfSize(ix, iy, isz):
                        largestMagicSquare = max(isz + 1, largestMagicSquare)
                    
                # for isz in range(len(targetSums[ix][iy]), maxSquareSize + 1): # len(targetSums[ix][iy]) == 1 here 
                #     # isz from 1 to 
                #     # squares to the left, above, and diagonal to the top left already have necessary sizes calc'd 
                #     horizTarg = targetSums[ix - 1][iy][isz - 1][HORIZ] + grid[ix][iy]
                #     vertTarg = targetSums[ix][iy - 1][isz - 1][VERT] + grid[ix][iy]
                #     tlbrDiagTarg = targetSums[ix - 1][iy - 1][isz - 1][TLBRDIAG] + grid[ix][iy]
                #     # TODO this needs to update the earlier squares, e.g. when ix == 0, as well 
                #     # bltrMaxSquareSize = min(iy, len(grid) - ix + 1) + 1
                #     # if (isz < bltrMaxSquareSize): bltrDiagTarg = targetSums[ix + 1][iy - 1][isz - 1][BLTRDIAG] + grid[ix][iy]
                #     # else: bltrDiagTarg = -1
                #     targetsBySizeHere = [horizTarg, vertTarg, tlbrDiagTarg, bltrDiagTarg]
                #     # if (targetsBySizeHere[:3])
                #     if all(map(lambda x: x == targetsBySizeHere[0], targetsBySizeHere[:BLTRDIAG])):
                #         if (all(map(lambda x: x == targetsBySizeHere[0], [targetSums[isx][iy][isz-len(targetSums[ix][iy])][VERT] for isx in range(1, isz)]))):
                #             if (all(map(lambda x: x == targetsBySizeHere[0], [targetSums[ix][isy][isz-len(targetSums[ix][iy])][HORIZ] for isy in range(1, isz)]))):
                #                 if (targetSums[ix - isz][iy][isz - 1][BLTRDIAG] == targetsBySizeHere[0]):
                #                     largestMagicSquare = max(isz, largestMagicSquare)

                # print(f"Before: {targetSums[ix][iy]}")
                # # targetSums[ix][iy].extend(targetsBySizeHere)
                # if targetsBySizeHere: targetSums[ix][iy].append(targetsBySizeHere)
                # print(f"After: {targetSums[ix][iy]}")

        return largestMagicSquare