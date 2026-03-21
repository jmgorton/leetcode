from typing import List

# class Solution:
#     def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
#         # tlbr = {}
#         # bltr = {}
#         m, n = len(grid), len(grid[0])
#         # for i in range(n):
#         #     tlbr[i] = {} # {i: grid[0][i]}
#         #     for j in range(1, min(n - i, m)):
#         #         tlbr[i + (j * m) + j] = {}
#         #     bltr[i] = {}

#         tops = {}
#         # for i in range(1, m - 1):
#         for i in range(m):
#             tops[i] = {}
#             # tops[i] = {j: {0: grid[0][j] for j in range(n)}} 
#             # for j in range(i, n - i):
#             for j in range(n):
#                 tops[i][j] = {}
#                 # grid[i][j] is center of rhombii stored in tops[i][j] dict
#                 # keys of tops[i][j] is the radii 
#                 for k in range(min(i + 1, m - i - 1, j + 1, n - j - 1)):
#                     if k: tops[i][j][k] = grid[i][j - k] + grid[i][j + k] + tops[i - 1][j][k - 1] 
#                     else: tops[i][j][k] = grid[i][j] 
        
#         bots = {}
#         best = []
#         # reflect up from the bottom and get the best values
#         for i in range(m):
#             bots[m - i - 1] = {}
#             for j in range(n):
#                 bots[m - i - 1][j] = {}
#                 for k in range(min(i + 1, m - i - 1, j + 1, n - j - 1)):
#                     if k: 
#                         bots[m - i - 1][j][k] = grid[m - i - 1][j - k] + grid[m - i - 1][j + k] + bots[m - i][j][k - 1]
#                         if k in tops[m - i - 1][j]: 
#                             heappush(best, -(bots[m - i][j][k - 1] + tops[m - i - 1][j][k]))
#                     else:
#                         bots[m - i - 1][j][k] = grid[i][j]
#                         heappush(best, -grid[i][j])

#         result = []
#         for _ in range(3):
#             if not best: break
#             result.append(-heappop(best))
#             while best and best[0] == -result[-1]: heappop(best) 
#         return result


class Answer:
    def __init__(self):
        self.ans = [0, 0, 0]

    def put(self, x: int):
        _ans = self.ans

        if x > _ans[0]:
            _ans[0], _ans[1], _ans[2] = x, _ans[0], _ans[1]
        elif x != _ans[0] and x > _ans[1]:
            _ans[1], _ans[2] = x, _ans[1]
        elif x != _ans[0] and x != _ans[1] and x > _ans[2]:
            _ans[2] = x

    def get(self) -> List[int]:
        _ans = self.ans

        return [num for num in _ans if num != 0]


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sum1 = [[0] * (n + 2) for _ in range(m + 1)]
        sum2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1]
                sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1]

        ans = Answer()
        for i in range(m):
            for j in range(n):
                # a single cell is also a rhombus
                ans.put(grid[i][j])
                for k in range(i + 2, m, 2):
                    ux, uy = i, j
                    dx, dy = k, j
                    lx, ly = (i + k) // 2, j - (k - i) // 2
                    rx, ry = (i + k) // 2, j + (k - i) // 2

                    if ly < 0 or ry >= n:
                        break

                    ans.put(
                        (sum2[lx + 1][ly + 1] - sum2[ux][uy + 2])
                        + (sum1[rx + 1][ry + 1] - sum1[ux][uy])
                        + (sum1[dx + 1][dy + 1] - sum1[lx][ly])
                        + (sum2[dx + 1][dy + 1] - sum2[rx][ry + 2])
                        - (
                            grid[ux][uy]
                            + grid[dx][dy]
                            + grid[lx][ly]
                            + grid[rx][ry]
                        )
                    )

        return ans.get()