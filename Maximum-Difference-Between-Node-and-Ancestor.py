# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recurse(smallest, largest, curr):
            smallest = min(smallest, curr.val)
            largest = max(largest, curr.val)
            if curr.left and curr.right:
                return max(recurse(smallest, largest, curr.left), recurse(smallest, largest, curr.right))
            elif curr.left:
                return recurse(smallest, largest, curr.left)
            elif curr.right:
                return recurse(smallest, largest, curr.right)
            else:
                return abs(largest - smallest)
        return recurse(root.val, root.val, root)