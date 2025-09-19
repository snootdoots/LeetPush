# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        curr_sum = 0
        while queue:
            num_elts_row = len(queue)
            my_sum = 0
            for _ in range(num_elts_row):
                curr = queue.pop(0)
                my_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            curr_sum = my_sum
        return curr_sum