from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # def __init__(self, tree: List[int]) -> Optional[TreeNode]:


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # # row-based iteration 
        # if not root: return True
        # curr = [root]
        # nxt = [root.left, root.right]
        # while all([x is not None for x in curr]):
        #     curr = nxt 
        #     nxt = [x.left if x else None for x in curr] + [x.right if x else None for x in curr]
        #     # print([x.val if x else None for x in curr], [x.val if x else None for x in nxt])
        # # return not any([x.left or x.right if x else None for x in nxt])
        # return not any(nxt)

        # recursive
        def depthAndBalance(node: TreeNode, nodeDepth: int) -> tuple[int, bool]:
            if not node: return (nodeDepth, True)
            # if not node.left and not node.right: return (1, True)
            lsd, lsb = depthAndBalance(node.left, nodeDepth + 1)
            rsd, rsb = depthAndBalance(node.right, nodeDepth + 1)
            return (max(lsd, rsd), lsb and rsb and abs(lsd - rsd) <= 1)
        d, b = depthAndBalance(root, 0)
        return b

tests = [
    {
        "in": [3,9,20,None,None,15,7],
        "out": True
    }
]

if __name__ == "__main__":
    sol = Solution()
    