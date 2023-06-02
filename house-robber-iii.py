# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    def dfs(self, node):
        if  not node:
            return 0, 0
        pprev1, prev1 = self.dfs(node.left)
        pprev2, prev2 = self.dfs(node.right)

        pprev = prev1 + prev2
        prev = max(pprev, pprev1 + pprev2 + node.val)

        return pprev, prev