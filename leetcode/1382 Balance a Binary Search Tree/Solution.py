from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we could just traverse the tree to get all the values,
        # then build a balanced tree from the sorted values
        # hmm, let's implement this too 

        # vals = []
        # def inorder(node):
        #     if not node: return
        #     inorder(node.left)
        #     vals.append(node.val)
        #     inorder(node.right)
        # inorder(root)

        # def buildBalancedTree(vals, left, right):
        #     if left > right: return None
        #     mid = (left + right) // 2
        #     node = TreeNode(vals[mid])
        #     node.left = buildBalancedTree(vals, left, mid - 1)
        #     node.right = buildBalancedTree(vals, mid + 1, right)
        #     return node
        # balancedRoot = buildBalancedTree(vals, 0, len(vals) - 1)
        # # return balancedRoot

        # but maybe a more fun approach... we can apply translations/rotations 
        # to the tree in-place for each unbalanced node,
        # similar to how we would balance an AVL tree after inserting a node
        # if not root: return root
        def translateListInputToTreeNode(root):
            if (type(root) == list): 
                print("List")
                # nodes = [TreeNode(v) if v is not None else None for v in root]
                # for i, v in enumerate(nodes):
                #     li = 2 * i + 1 # this is incorrect according to lc input format 
                #     ri = 2 * i + 2 # incorrect according to lc input format
                #     if v is not None:
                #         # root[i] = TreeNode(v)
                #         v.left = nodes[li] if li < len(nodes) else None
                #         v.right = nodes[ri] if ri < len(nodes) else None
                # return nodes[0] if nodes else None
                nodes = [TreeNode(root[0]) if root[0] is not None else None]
                queue = [nodes[0]]
                i = 1
                while queue and i < len(root):
                    node = queue.pop(0)
                    if node is None:
                        continue
                    if i < len(root):
                        left_val = root[i]
                        i += 1
                        node.left = TreeNode(left_val) if left_val is not None else None
                        queue.append(node.left)
                    if i < len(root):
                        right_val = root[i]
                        i += 1
                        node.right = TreeNode(right_val) if right_val is not None else None
                        queue.append(node.right)
                return nodes[0]
            elif (type(root) == TreeNode): 
                print("TreeNode")
                return root
            # if (isinstance(root, list)): print("List")
            # elif (isinstance(root, TreeNode)): print("TreeNode")
            # type() checks the exact class type, while isinstance() supports inheritance, making it more versatile.
        root = translateListInputToTreeNode(root)

        def translateTreeNodeToList(root):
            if not root: return None
            result = []
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            # Remove trailing None values to match expected output format
            while result and result[-1] is None:
                result.pop()
            return result

        # def depthAndBalance(node: TreeNode, nodeDepth: int) -> tuple[int, TreeNode]:
        #     if not node: return (nodeDepth, None)
        #     lsd, lsr = depthAndBalance(node.left, nodeDepth + 1)
        #     rsd, rsr = depthAndBalance(node.right, nodeDepth + 1)
        #     node.left = lsr
        #     node.right = rsr
        #     newRoot = node
        #     while lsd - rsd > 1:
        #         # left-heavy, rotate right
        #         # print(f"Rotating right at node {node.val} with lsd {lsd} and rsd {rsd}")
        #         newRoot = node.left # left child will be new root
        #         node.left = newRoot.right # left child's right subtree becomes left subtree of current node
        #         newRoot.right = node # current node becomes right child of left child
        #         node = newRoot
        #         # lsd -= 1
        #         lsd, lsr = depthAndBalance(node.left, nodeDepth + 1)
        #         # rsd += 1
        #         rsd, rsr = depthAndBalance(node.right, nodeDepth + 1)
        #     while rsd - lsd > 1:
        #         # right-heavy, rotate left
        #         # print(f"Rotating left at node {node.val} with lsd {lsd} and rsd {rsd}")
        #         newRoot = node.right
        #         node.right = newRoot.left
        #         newRoot.left = node
        #         node = newRoot
        #         # lsd += 1
        #         lsd, lsr = depthAndBalance(node.left, nodeDepth + 1)
        #         # rsd -= 1
        #         rsd, rsr = depthAndBalance(node.right, nodeDepth + 1)
        #     return max(lsd, rsd), newRoot
        # _, root = depthAndBalance(root, 0)
        # # return root
        # return translateTreeNodeToList(root)
    
        ## AI solution:
        # AVL-style balancing (in-place rotations)
        height = {}

        def h(node):
            return height.get(node, 0) if node else 0

        # def update(node):
        #     height[node] = 1 + max(h(node.left), h(node.right))
        
        def recalc(node):
            if not node:
                return 0
            hl = recalc(node.left)
            hr = recalc(node.right)
            height[node] = 1 + max(hl, hr)
            return height[node]

        def rotate_right(y):
            x = y.left
            t2 = x.right
            x.right = y
            y.left = t2
            recalc(y) # update heights after rotation
            recalc(x)
            return x

        def rotate_left(x):
            y = x.right
            t2 = y.left
            y.left = x
            x.right = t2
            # update(x)
            # update(y)
            recalc(x) # update heights after rotation
            recalc(y)
            return y

        def rebalance(node):
            if not node:
                return None
            node.left = rebalance(node.left)
            node.right = rebalance(node.right)

            while True:
                # update(node)
                recalc(node)
                balance = h(node.left) - h(node.right)

                if balance > 1:
                    # Left heavy
                    if h(node.left.left) < h(node.left.right):
                        node.left = rotate_left(node.left)
                        recalc(node.left) # update height after rotation
                    # return rotate_right(node)
                    node = rotate_right(node)
                    continue

                if balance < -1:
                    # Right heavy
                    if h(node.right.right) < h(node.right.left):
                        node.right = rotate_right(node.right)
                        recalc(node.right) # update height after rotation
                    # return rotate_left(node)
                    node = rotate_left(node)
                    continue

                return node

        root = rebalance(root)
        # return root
        return translateTreeNodeToList(root)
    
    ### Your AVL-style “one postorder pass” still doesn’t guarantee
    #  full balance for an arbitrary BST. AVL rotations are correct 
    # when balancing after insertions, because only the insertion 
    # path can become unbalanced. Here, every node can be arbitrarily 
    # skewed, so a single bottom‑up pass can leave some nodes (like 
    # the left child of your root) still outside {−1,0,1} even after 
    # local rotations.
    ### That’s why the left subtree stays a right‑leaning chain in 
    #  your output: the algorithm isn’t designed for “rebalancing a 
    # fully arbitrary BST” in one pass.
    ### If you want a true in‑place balancing algorithm without 
    #  rebuilding from inorder, use the Day–Stout–Warren (DSW) 
    # algorithm: it transforms the tree into a “vine” (right‑skewed 
    # list) and then compresses it into a balanced tree using 
    # rotations. That’s guaranteed to balance any BST in-place.
    
tests = [
    {
        "in": [1,None,2,None,3,None,4,None,None],
        "out": [[2,1,3,None,None,None,4], [3,1,4,None,2], [2,1,4,None,None,3], [3,2,4,1]]
    },
    {
        "in": [2,1,3],
        "out": [[2,1,3]]
    },
    {
        "in": [1,None,15,14,17,7,None,None,None,2,12,None,3,9,None,None,None,None,11],
        # "out": [[7,2,15,1,None,14,17,None,None,3,12,None,None,None,None,None,None,None,None,9
        "out": [[9,2,14,1,3,11,15,None,None,None,7,None,12,None,17]]
    }
]

# the test cases i'm using aren't exactly the same as the ones on leetcode
# for example, test case 1 is [1,null,2,null,3,null,4,null,null] which
# indicates that only non-null nodes and potential null children are included
# in the input, whereas i thought each row of the tree would be fully 
# represented in the input list, with nulls for missing nodes
if __name__ == "__main__":
    sol = Solution()
    for test in tests:
        assert (actual := sol.balanceBST(test["in"])) in test["out"], f"Test failed: expected one of: {test['out']}; got {actual}"
    print("All tests passed!")