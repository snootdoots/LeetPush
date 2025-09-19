# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def recurse(curr_max, root):
            if not root:
                return 0
            left = recurse(1+curr_max, root.left)
            right = recurse(1+curr_max, root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        recurse(0, root)
        return self.diameter