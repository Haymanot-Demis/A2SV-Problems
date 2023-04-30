# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        return int(result[1])
    def dfs(self, node):
        if not node:
            return 0, -2**31
        left, max_path_sum1 = self.dfs(node.left)
        right, max_path_sum2 = self.dfs(node.right)
        path_sum = max(left, right) + node.val

        if path_sum < node.val:
            path_sum = node.val

        max_path_sum =  max(max_path_sum1, max_path_sum2, path_sum, left + right + node.val)
        
        return path_sum, max_path_sum