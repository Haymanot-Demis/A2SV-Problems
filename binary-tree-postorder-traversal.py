# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node, values):
            if node:
                postorder(node.left, values)
                postorder(node.right, values)
                values.append(node.val)
            return values
        return postorder(root, [])