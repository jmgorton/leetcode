from typing import List

### Hint 1: Try to solve this without using the '/' (division operation).

### Hint 2: Create two 2D arrays for suffix and prefix product, and use them to find the product for each position.

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        prod = 1
        pre = []
        for row in grid:
            pre.append([])
            for el in row:
                prod *= el
                prod %= 12345
                pre[-1].append(prod) 
        
        prod = 1
        post = []
        for row in grid[::-1]:
            post.append([])
            for el in row[::-1]:
                prod *= el
                prod %= 12345
                post[-1].append(prod)
            post[-1] = post[-1][::-1]
        post = post[::-1]

        result = []
        for i in range(len(grid)):
            result.append([])
            for j in range(len(grid[i])):
                prod = 1
                if j: prod *= pre[i][j - 1]
                elif i: prod *= pre[i - 1][-1]
                if j < len(grid[i]) - 1: prod *= post[i][j + 1]
                elif i < len(grid) - 1: prod *= post[i + 1][0]
                prod %= 12345
                result[-1].append(prod) 
        
        return result 

        # tp = math.prod(math.prod(row) for row in grid) % 12345
        # tp = 1
        # s = set()
        # for row in grid:
        #     for el in row:
        #         tp *= el
        #         # tp %= 12345
        #         s.add(el)
        # lk = {x: (tp // x) % 12345 for x in s}
        # # lk = {None: 1}
        # # for row in grid:
        # #     for el in row:
        # #         if el not in lk:
        # #             lke = lk[None]
        # #             lk = {x: (v * el) % 12345 for x, v in lk.items()}
        # #             lk[el] = lke
        # #         else:
        # #             lk = {x: (v * el) % 12345 for x, v in lk.items()}

        # return [[lk[x] for x in row] for row in grid]
