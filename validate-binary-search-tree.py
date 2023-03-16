# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, values):
            if node:
                inorder(node.left, values)
                values.append(node.val)
                inorder(node.right, values)
            return values
        values = inorder(root, [])
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True