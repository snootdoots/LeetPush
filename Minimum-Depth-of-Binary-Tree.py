# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def recurse(root):
            if root.left and root.right:
                return min(1+recurse(root.left), 1+recurse(root.right))
            elif root.left:
                return 1+recurse(root.left)
            elif root.right:
                return 1+recurse(root.right)
            else:
                return 1
        return recurse(root)