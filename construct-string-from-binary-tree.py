# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)

    def dfs(self, node):
        if not node.left and not node.right:
            return str(node.val)
        if not node.left:
            string = self.dfs(node.right)
            return str(node.val) + "(" + ")" + "(" + string + ")"
        if not node.right:
            string = self.dfs(node.left)
            return str(node.val) + "(" + string + ")"

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return str(node.val) + "(" + left + ")" + "(" + right + ")"