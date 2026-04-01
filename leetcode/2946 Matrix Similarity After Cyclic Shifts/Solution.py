from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat) 
        cols = len(mat[0])
        for i, row in enumerate(mat):
            for j, el in enumerate(row):
                if i % 2: 
                    if mat[i][(j + k) % cols] != el: return False
                else: 
                    if mat[i][(j - k) % cols] != el: return False
        return True