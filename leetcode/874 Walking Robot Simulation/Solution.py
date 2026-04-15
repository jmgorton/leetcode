from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = (0, 0) 
        ori = (0, 1) 

        obs = {(x, y): True for x, y in obstacles}
        # obs = {}
        # for x, y in obstacles:
        #     obs[(x, y)] = True

        # def move(pos, ori, op) -> tuple:
        def move(pos, ori) -> tuple:
            dest = (pos[0] + ori[0], pos[1] + ori[1])
            if dest in obs: return pos
            return dest
        
        def turn(ori, cw) -> tuple:
            newX = 0 if ori[0] else 1
            if ori[1] == 1 and not cw: newX = -1
            if ori[1] == -1 and cw: newX = -1
            newY = 0 if ori[1] else 1
            if ori[0] == 1 and cw: newY = -1
            if ori[0] == -1 and not cw: newY = -1
            return (newX, newY)
        
        best = 0 
        for c in commands:
            if c == -1: ori = turn(ori, True)
            elif c == -2: ori = turn(ori, False)
            else:
                for _ in range(c):
                    pos = move(pos, ori)
                best = max(best, pos[0] ** 2 + pos[1] ** 2)
        return best
