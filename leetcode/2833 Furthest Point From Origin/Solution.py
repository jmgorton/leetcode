class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # best = [0, 0]
        curr = [0, 0]

        for c in moves:
            if c == 'L': 
                curr[0] -= 1
                curr[1] -= 1
            elif c == 'R':
                curr[0] += 1
                curr[1] += 1
            else:
                curr[0] -= 1
                curr[1] += 1

            # print(curr)
            # best[0] = min(best[0], curr[0])
            # best[1] = max(best[1], curr[1])
        
        return max(-curr[0], curr[1])