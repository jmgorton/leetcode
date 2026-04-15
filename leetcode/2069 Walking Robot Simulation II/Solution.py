# class Robot:

#     def __init__(self, width: int, height: int):
#         self.pos = (0, 0) 
#         self.ori = (1, 0) 
#         self.width = width
#         self.height = height
    
#     def _move(self) -> None:
#         newPos = (self.pos[0] + self.ori[0], self.pos[1] + self.ori[1])
#         if -1 < newPos[0] < self.width and -1 < newPos[1] < self.height: self.pos = newPos
#         else: 
#             self._turn()
#             self._move() # infinite loop impossible ... i think? 
    
#     def _turn(self) -> None:
#         newX = 0 if self.ori[0] else 1
#         if self.ori[1] == 1: newX = -1
#         newY = 0 if self.ori[1] else 1
#         if self.ori[0] == -1: newY = -1
#         self.ori = (newX, newY)

#     def step(self, num: int) -> None:
#         for _ in range(num):
#             self._move()

#     def getPos(self) -> List[int]:
#         return list(self.pos)

#     def getDir(self) -> str:
#         match self.ori:
#             case (1, 0): return "East"
#             case (0, 1): return "North"
#             case (-1, 0): return "West"
#             case (0, -1): return "South"
#             case _: return ""


### Official solution? 

from typing import List

# # Your Robot object will be instantiated and called as such:
# # obj = Robot(width, height)
# # obj.step(num)
# # param_2 = obj.getPos()
# # param_3 = obj.getDir()

class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = list()
        self.dirs = list()

        pos_, dirs_ = self.pos, self.dirs

        for i in range(width):
            pos_.append((i, 0))
            dirs_.append(0)
        for i in range(1, height):
            pos_.append((width - 1, i))
            dirs_.append(1)
        for i in range(width - 2, -1, -1):
            pos_.append((i, height - 1))
            dirs_.append(2)
        for i in range(height - 2, 0, -1):
            pos_.append((0, i))
            dirs_.append(3)

        dirs_[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.idx])

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]