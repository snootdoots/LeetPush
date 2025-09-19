# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        backwards = False
        return_q = []
        while queue:
            nodes_curr_level = len(queue)
            curr_level = []
            for _ in range(nodes_curr_level):
                curr = queue.pop(0)
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if backwards:
                curr_level.reverse()
            return_q.append(curr_level)
            if backwards:
                backwards = False
            else:
                backwards = True
        return return_q