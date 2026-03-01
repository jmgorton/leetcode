from typing import Optional, List
from itertools import zip_longest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # get depths of all leaves from node
        # sum each node according to depth/bit 
        def countLeafDepths(node: Optional[TreeNode]) -> List[int]:
            if not node: return []
            if not node.left and not node.right: 
                node.leafDepths = [1]
            else:
                lld = countLeafDepths(node.left) 
                rld = countLeafDepths(node.right) 
                node.leafDepths = [0] + [x + y for x, y in zip_longest(lld, rld, fillvalue=0)]
            return node.leafDepths

        countLeafDepths(root) 

        def sumByLeafDepths(node: Optional[TreeNode]) -> int:
            if not node: return 0
            result = sumByLeafDepths(node.left) + sumByLeafDepths(node.right) 
            if node.val == 1:
                mult = 1
                for v in node.leafDepths:
                    result += v * mult
                    mult <<= 1
            return result
        
        return sumByLeafDepths(root) 
        