# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        curr_level = 0
        return_arr = []
        queue = [root]
        while queue:
            curr_nodes_count = len(queue)
            return_arr.append(0)
            for _ in range(curr_nodes_count):
                curr = queue.pop(0)
                return_arr[curr_level] = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            curr_level += 1
        return return_arr