# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(curr, currmax):
            if curr is None:
                return 0
            addition = 0
            if curr.val >= currmax:
                addition += 1
            
            return addition + helper(curr.left, max(currmax, curr.val)) + helper(curr.right, max(currmax, curr.val))
        return helper(root, root.val)
        